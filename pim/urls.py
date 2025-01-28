from django.urls import path
from . import views

app_name = 'pim'

urlpatterns = [
    path('add/', views.ProductCreateView.as_view(), name='add'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
]