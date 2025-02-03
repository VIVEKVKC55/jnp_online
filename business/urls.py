from django.urls import path
from .views import register_business, BusinessDetailsUpdateView, BusinessDetailsCreateView

app_name = 'business'

urlpatterns = [
    path('new_reg/', register_business, name='new_reg'),
    path('update/', BusinessDetailsUpdateView.as_view(), name='update'),
    path('register/', BusinessDetailsCreateView.as_view(), name='business-register'),
    path('update/<int:pk>/', BusinessDetailsUpdateView.as_view(), name='business_update'),
]
