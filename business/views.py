from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BusinessDetailsForm, BusinessDetailsUpdateForm
from .models import BusinessDetails
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

def register_user(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            # Save user and business registration details
            
            business_registration = form.save(commit=False)
            business_registration.save()

            # Send email to the admin after successful registration
            send_mail(
                'New User Registration',
                f'Hello Admin,\n\nA new user has registered with the business name: {business_registration.business_name}. '
                'Please review and approve the registration.\n\n'
                'To approve, please log in to the admin panel and update the approval status.\n\n'
                f'https://jnp-online.vercel.app/admin/business/businessdetails/{business_registration.id}/change/'
                '\n\nRegards,\nYour Website',
                settings.DEFAULT_FROM_EMAIL,  # From email address
                [settings.ADMIN_EMAIL],  # To email address (Admin's email)
                fail_silently=False,
            )
                        # Send an email to the user confirming registration
            send_mail(
                'Registration Successful',
                f'Hello {business_registration.user.username},\n\n'
                'Your registration has been successfully received. Your business registration is now pending approval.\n\n'
                'You will be notified once your registration is approved.\n\n'
                'Regards,\nYour Website',
                settings.DEFAULT_FROM_EMAIL,  # From email address
                [business_registration.user.email],  # To email address (User's email)
                fail_silently=False,
            )

            messages.success(request, "Registration successful. Please log in.")
            return redirect('account:login')
        else:
            messages.error(request, "There was an error with the registration form.")
    else:
        form = BusinessDetailsForm()
    return render(request, 'default/business/register.html', {'form': form})


class BusinessDetailsUpdateView(UpdateView):
    model = BusinessDetails
    form_class = BusinessDetailsUpdateForm  # Form for updating business details
    template_name = 'default/business/edit.html'
    context_object_name = 'business_details'
    success_url = reverse_lazy('pim:list')  # Redirect to a list page after successful update

    def get_object(self, queryset=None):
        """ Fetch the BusinessDetails object associated with the current user """
        try:
            return self.request.user.businessdetails
        except BusinessDetails.DoesNotExist:
            # Handle the case where the user does not have business details
            messages.error(self.request, "You don't have business details associated with your account.")
            return redirect('home:home')  # Or another appropriate page

    def form_valid(self, form):
        """ Handle form submission when valid """
        # Save the business details
        business_details = form.save()

        # Send email to the admin after the business details are updated
        send_mail(
            'Business Details Updated',
            f'Hello Admin,\n\nA user has updated their business details. The business name is: {business_details.business_name}. '
            'Please review and approve the updated information.\n\n'
            f'https://jnp-online.vercel.app/admin/business/businessdetails/{business_details.id}/change/\n\n'
            'Regards,\nYour Website',
            settings.DEFAULT_FROM_EMAIL,  # From email address
            [settings.ADMIN_EMAIL],  # Admin's email address
            fail_silently=False,
        )

        # Send an email to the user confirming their business details update
        send_mail(
            'Business Details Update Successful',
            f'Hello {business_details.user.username},\n\n'
            'Your business details have been successfully updated and are now pending approval.\n\n'
            'You will be notified once your registration is approved or further action is required.\n\n'
            'Regards,\nYour Website',
            settings.DEFAULT_FROM_EMAIL,  # From email address
            [business_details.user.email],  # User's email address
            fail_silently=False,
        )

        messages.success(self.request, "Your business details have been updated successfully and are pending approval.")
        return redirect(self.success_url)

    def form_invalid(self, form):
        """ Handle invalid form submission """
        messages.error(self.request, "There was an error with updating your business details.")
        return super().form_invalid(form)
