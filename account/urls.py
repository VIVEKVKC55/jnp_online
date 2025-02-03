from django.urls import path
from . import views
from .cus_view import wishlist

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.customer_login, name='login'),
    path('logout/', views.logout_view, name='logout'),  # This is to logout the user

    path('wishlist/', wishlist.WishlistView.as_view(), name='wishlist'),
    path('wishlist/toggle/<int:pk>/', wishlist.ToggleWishlistView.as_view(), name='toggle_wishlist'),
]
