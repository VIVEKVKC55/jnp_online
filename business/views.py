from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
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
        form = RegistrationForm()
    return render(request, 'default/business/register.html', {'form': form})

