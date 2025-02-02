from django.urls import path
from .views import register_user,BusinessDetailsUpdateView

app_name = 'business'

urlpatterns = [
    path('reg/', register_user, name='reg'),
    path('update/', BusinessDetailsUpdateView.as_view(), name='update'),
    path('update/<int:pk>/', BusinessDetailsUpdateView.as_view(), name='business_update'),
]
