from django.contrib import admin
from .models import Category, ProductBrand,ProductAttributes, ProductImages

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'parent', 'created', 'created_by', 'updated', 'updated_by')
    search_fields = ('name', 'slug')
    list_filter = ('created', 'updated')

@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'created_by', 'updated', 'updated_by')
    search_fields = ('name', 'slug')
    list_filter = ('created', 'updated')


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'full_url', 'title', 'is_enabled', 'is_default', 'order_by', 'created')
    search_fields = ('title', 'caption', 'product__name')
    list_filter = ('is_enabled', 'is_default', 'created')
    ordering = ('order_by', 'id')  # Order by the `order_by` field and ID
    list_editable = ('is_enabled', 'is_default', 'order_by')  # Allow inline editing
    readonly_fields = ('created',)  # Prevent editing the auto-updated `created` field

@admin.register(ProductAttributes)
class ProductAttributesAdmin(admin.ModelAdmin):
    """Customize the ProductAttributes admin interface."""
    list_display = ('id', 'attribute_name', 'is_default')
    list_filter = ('is_default',)  # Filter by default status
    search_fields = ('attribute_name',)  # Enable search by attribute name
    ordering = ('id',)  # Order by ID
