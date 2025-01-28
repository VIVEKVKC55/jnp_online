from django.contrib import admin
from .models import Category, ProductBrand, Product, ProductImages,ProductAttributes, ProductAttributeValue

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category_group_id', 'parent', 'created', 'created_by', 'updated', 'updated_by')
    search_fields = ('name', 'slug')
    list_filter = ('created', 'updated')

@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'created_by', 'updated', 'updated_by')
    search_fields = ('name', 'slug')
    list_filter = ('created', 'updated')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'brand', 'is_deleted', 'is_enabled', 'created', 'created_by', 'updated', 'updated_by')
    search_fields = ('name', 'slug')
    list_filter = ('is_enabled', 'is_best_seller', 'is_home_featured', 'is_featured', 'created', 'updated')


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


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    """Customize the ProductPartAttributeValue admin interface."""
    list_display = ('id', 'product', 'attribute', 'attribute_value', 'order_no')
    list_filter = ('attribute',)  # Filter by attribute type
    search_fields = ('product_part__name', 'attribute__attribute_name', 'attribute_value')  # Enable search
    ordering = ('order_no',)  # Default ordering by `order_no`

    autocomplete_fields = ('product', 'attribute') 


