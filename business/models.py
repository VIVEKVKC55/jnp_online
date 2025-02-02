from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

class BusinessDetails(models.Model):
    TYPE_OF_BUSINESS_CHOICES = [
        ('Importer', 'Importer'),
        ('Trader', 'Trader'),
        ('Both', 'Both'),
    ]
    
    DEALING_WITH_CHOICES = [
        ('Laptops', 'Laptops'),
        ('Spare Parts', 'Spare Parts'),
        ('Both', 'Both'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    business_location = models.CharField(max_length=255)
    type_of_business = models.CharField(max_length=20, choices=TYPE_OF_BUSINESS_CHOICES)
    dealing_with = models.CharField(max_length=20, choices=DEALING_WITH_CHOICES)
    business_name_board_photo = CloudinaryField('business_photos')
    authorized_person_photo = CloudinaryField('authorized_person_photos')
    mobile_number = models.CharField(max_length=15)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_businesses")

    def toggle_approval(self, approver):
        """Toggle approval status and record the approver."""
        self.is_approved = not self.is_approved
        self.approved_by = approver if self.is_approved else None
        self.save()

    def __str__(self):
        return self.business_name
    class Meta:
        """Provide database table name explicitly."""

        db_table = 'businuss_details'