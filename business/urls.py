from django.urls import path
from .views import register_user,BusinessDetailsUpdateView

app_name = 'busniuss'

urlpatterns = [
    path('reg/', register_user, name='reg'),
    path('update/', BusinessDetailsUpdateView.as_view(), name='update'),
]
