from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404
from business.models import BusinessDetails
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings


class BusinessDetailsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    View to list all business details.
    Access is restricted to staff and superusers.
    """
    model = BusinessDetails
    template_name = 'admin/business/list.html'  # HTML template to display the list
    context_object_name = 'businesses'

    def test_func(self):
        """Restrict access to staff and superusers only."""
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_queryset(self):
        """
        Order businesses by approval status (approved first) and creation date (newest first).
        """
        return BusinessDetails.objects.all().order_by('-is_approved', '-id')  # Replace `id` with `created_at` if available


class BusinessDetailPopupView(DetailView):
    model = BusinessDetails
    template_name = 'admin/business/details_popup.html'
    context_object_name = 'business'

    def get_object(self):
        """Override to retrieve business details based on URL parameter"""
        business_id = self.kwargs['business_id']
        return get_object_or_404(BusinessDetails, id=business_id)
    

class ToggleBusinessApprovalView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Class-based view to approve/unapprove business details"""

    def test_func(self):
        """Ensure only is_staff or is_superuser can perform this action"""
        return self.request.user.is_superuser or self.request.user.is_staff

    def post(self, request, business_id):
        """Approve or unapprove the business"""
        # Check if the user is allowed to perform the action
        if not self.test_func():
            return JsonResponse({"error": "You don't have permission to perform this action."}, status=403)
        
        business = get_object_or_404(BusinessDetails, id=business_id)
        
        # Call the toggle_approval method on the business model
        business.toggle_approval(request.user)
        
        # Send email to the business owner after approval/unapproval
        subject = 'Your Business Approval Status has Changed'
        email_message = f'Hello {business.owner_name},\n\n' \
                  f'Your business "{business.business_name}" has been {'approved' if business.is_approved else 'unapproved'} by {request.user.username}.\n\n' \
                  'Thank you for your cooperation.'
        from_email = settings.DEFAULT_FROM_EMAIL  # Make sure to set this in your settings.py
        recipient_list = [business.user.email]  # Assuming mobile_number is an email field (if not, adjust accordingly)

        # Send the email
        send_mail(subject, email_message, from_email, recipient_list)

        return JsonResponse({
            "success": True, 
            "is_approved": business.is_approved, 
            "approved_by": business.approved_by.username if business.approved_by else None
        })

