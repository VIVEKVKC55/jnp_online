from django import forms
from django.contrib.auth.models import User
from .models import BusinessDetails

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = BusinessDetails
        fields = [
            'business_name', 'address', 'owner_name', 'authorized_person_name',
            'business_location', 'type_of_business', 'dealing_with',
            'business_name_board_photo', 'authorized_person_photo', 'mobile_number', 'email_id'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data

    def save(self, commit=True):
        # Get the cleaned data from the form
        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        email = cleaned_data.get("email_id")

        # Create a new User instance or update if needed
        user = User.objects.create_user(
            username=email,  # Use email as the username for the user
            email=email,
            password=password
        )

        # Now create or update the BusinessRegistration instance
        business_registration = super().save(commit=False)
        business_registration.user = user  # Associate the user with the business registration

        if commit:
            business_registration.save()

        return business_registration

