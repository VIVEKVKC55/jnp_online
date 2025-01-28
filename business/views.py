from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save user and business registration details
            user = User.objects.create_user(
                username=form.cleaned_data['email_id'],
                email=form.cleaned_data['email_id'],
                password=form.cleaned_data['password']
            )
            business_registration = form.save(commit=False)
            business_registration.user = user
            business_registration.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('account:login')
        else:
            messages.error(request, "There was an error with the registration form.")
    else:
        form = RegistrationForm()
    return render(request, 'default/business/register.html', {'form': form})

