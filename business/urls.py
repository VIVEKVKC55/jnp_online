from django.urls import path
from .views import register_user

app_name = 'business'

urlpatterns = [
    path('business_register/', register_user, name='business_register'),
]
