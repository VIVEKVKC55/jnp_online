from django import forms
from django.contrib.auth.models import User
from .models import BusinessRegistration

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = BusinessRegistration
        fields = [
            'business_name', 'address', 'owner_name', 'authorized_person_name',
            'business_location', 'type_of_business', 'dealing_with',
            'business_name_board_photo', 'authorized_person_photo', 'mobile_number', 'email_id'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
