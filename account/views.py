from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def register(request):
    """
    Handle the registration of a new customer.
    """
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_superuser = False  # Ensure the user is not a superuser
            user.is_staff = False  # Ensure the user is not a staff member
            user.save()

            # Automatically log the user in
            login(request, user)

            # Send email to the user
            send_mail(
                'Registration Successful',
                f'Hello {user.username},\n\nYour registration was successful. Welcome to our platform!\n\nBest Regards,\nYour Website Team',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            # # Send email to admin
            # send_mail(
            #     'New User Registered',
            #     f'Hello Admin,\n\nA new user has registered.\nUsername: {user.username}\nEmail: {user.email}\n\nPlease review their details.\n\nBest Regards,\nYour Website',
            #     settings.DEFAULT_FROM_EMAIL,
            #     [settings.ADMIN_EMAIL],  # Admin email from settings
            #     fail_silently=False,
            # )

            messages.success(request, "Registration successful! You are now logged in.")
            return redirect(reverse_lazy('account:login'))  # Redirect to the login page or dashboard
    else:
        form = CustomerRegistrationForm()

    return render(request, 'default/account/reg.html', {'form': form})


def customer_login(request):
    """
    Handle customer login.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            
            # Check if there is a 'next' parameter, otherwise default to home
            next_url = request.GET.get('next', reverse_lazy('home:home'))
            return redirect(next_url)  # Redirect to the original page or home
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'default/account/login.html')

def logout_view(request):
    """
    Handle customer logout.
    """
    logout(request)
    return redirect('account:login')  # Redirect to login page after logging out

