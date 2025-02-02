from django.urls import path
from . import views, admin_staff

app_name = 'pim'

urlpatterns = [
    path('add/', views.ProductCreateView.as_view(), name='add'),
    path('list/', views.ProductListView.as_view(), name='list'),
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
    path('edit_images/<int:pk>/', views.ProductImageUpdateView.as_view(), name='edit_images'),
    path('edit_attribute/<int:pk>/', views.ProductAttributeUpdateView.as_view(), name='edit_attribute'),


    path('admin/businesses/', admin_staff.BusinessDetailsListView.as_view(), name='business_list'),
    path('businesses/<int:business_id>/popup/', admin_staff.BusinessDetailPopupView.as_view(), name='business_detail_popup'),
    path('toggle_approval/<int:business_id>/', admin_staff.ToggleBusinessApprovalView.as_view(), name='toggle_business_approval'),

    path('products/', admin_staff.ProductListView.as_view(), name='product_list'),
    path('products/<int:product_id>/details/', admin_staff.ProductDetailPopupView.as_view(), name='product_detail_popup'),
    path('products/<int:product_id>/toggle-approval/', admin_staff.ToggleProductApprovalView.as_view(), name='toggle_product_approval'),
]