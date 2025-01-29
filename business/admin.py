from django.contrib import admin
from .models import BusinessDetails
from .forms import RegistrationForm

@admin.register(BusinessDetails)
class BusinessRegistrationAdmin(admin.ModelAdmin):
    form = RegistrationForm  # Use the custom form
    
    list_display = ('business_name', 'owner_name', 'authorized_person_name', 'type_of_business', 'dealing_with', 'mobile_number', 'email_id')
    search_fields = ('business_name', 'owner_name', 'authorized_person_name', 'mobile_number', 'email_id')
    list_filter = ('type_of_business', 'dealing_with')

    def save_model(self, request, obj, form, change):
        form.save()  # This will handle saving the user and business registration together
        super().save_model(request, obj, form, change)
