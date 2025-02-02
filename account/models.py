from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'customer'