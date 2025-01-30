from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    
    path('list/', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.CategoryProductView.as_view(), name='cat_products'),
]