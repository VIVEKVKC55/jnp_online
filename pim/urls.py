from django.urls import path
from . import views

app_name = 'pim'

urlpatterns = [
    path('add/', views.ProductCreateView.as_view(), name='add'),
    path('list/', views.ProductListView.as_view(), name='list'),
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
    path('edit_images/<int:pk>/', views.ProductImageUpdateView.as_view(), name='edit_images'),
    path('edit_attribute/<int:pk>/', views.ProductAttributeUpdateView.as_view(), name='edit_attribute'),
]