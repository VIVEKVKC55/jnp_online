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



from catalog.models import Product

class ProductListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    View to list all products.
    Access is restricted to staff and superusers.
    """
    model = Product
    template_name = 'admin/product/list.html'  # HTML template to display the list
    context_object_name = 'products'

    def test_func(self):
        """Restrict access to staff and superusers only."""
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_queryset(self):
        """
        Order products by approval status (approved first) and creation date (newest first).
        """
        return Product.objects.all().order_by('-is_approved', '-created')  # Adjust ordering as needed


class ProductDetailPopupView(DetailView):
    model = Product
    template_name = 'admin/product/details_popup.html'  # Template to display product details in modal
    context_object_name = 'product'

    def get_object(self):
        """Override to retrieve product details based on URL parameter"""
        product_id = self.kwargs['product_id']
        return get_object_or_404(Product, id=product_id)


class ToggleProductApprovalView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Class-based view to approve/unapprove product details"""

    def test_func(self):
        """Ensure only staff or superuser can perform this action"""
        return self.request.user.is_superuser or self.request.user.is_staff

    def post(self, request, product_id):
        """Approve or unapprove the product"""
        # Check if the user is allowed to perform the action
        if not self.test_func():
            return JsonResponse({"error": "You don't have permission to perform this action."}, status=403)
        
        product = get_object_or_404(Product, id=product_id)
        
        # Toggle the approval status of the product
        product.is_approved = not product.is_approved
        product.approved_by = request.user if product.is_approved else None
        product.save()

        # Send email to the product creator after approval/unapproval
        subject = 'Your Product Approval Status has Changed'
        email_message = f'Hello {product.created_by.username},\n\n' \
                        f'Your product "{product.name}" has been {'approved' if product.is_approved else 'unapproved'} by {request.user.username}.\n\n' \
                        'Thank you for your cooperation.'
        from_email = settings.DEFAULT_FROM_EMAIL  # Ensure this is set in settings.py
        recipient_list = [product.created_by.email]

        # Send the email
        send_mail(subject, email_message, from_email, recipient_list)

        return JsonResponse({
            "success": True,
            "is_approved": product.is_approved,
            "approved_by": product.approved_by.username if product.approved_by else None
        })
