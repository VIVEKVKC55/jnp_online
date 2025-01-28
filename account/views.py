from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import CustomerRegistrationForm
from django.contrib import messages


def register(request):
    """
    Handle the registration of a new customer.
    """
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object but do not assign superuser or staff privileges
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_superuser = False  # Ensure the user is not a superuser
            user.is_staff = False  # Ensure the user is not a staff member
            user.save()

            # Automatically log the user in
            login(request, user)

            messages.success(request, "Registration successful! You are now logged in.")
            return redirect(reverse_lazy('account:login'))  # Redirect to a home page or product listing page
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

