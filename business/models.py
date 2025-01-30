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

    def __str__(self):
        return self.business_name
    class Meta:
        """Provide database table name explicitly."""

        db_table = 'businuss_details'