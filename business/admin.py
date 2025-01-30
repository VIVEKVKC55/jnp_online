from django.contrib import admin
from .models import BusinessDetails

@admin.register(BusinessDetails)
class BusinessRegistrationAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'owner_name', 'type_of_business', 'dealing_with', 'mobile_number')
    search_fields = ('business_name', 'owner_name', 'mobile_number', )
    list_filter = ('type_of_business', 'dealing_with')
    # readonly_fields = ('user',)  # Make the user field read-only as it's automatically created
    fields = ('user', 'business_name', 'address', 'owner_name', 'business_location', 'type_of_business', 'dealing_with', 'business_name_board_photo', 'authorized_person_photo', 'mobile_number')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the business registration is being created, set the user
            obj.user = request.user
        super().save_model(request, obj, form, change)
