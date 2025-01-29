from django.contrib import admin
from .models import Category, ProductBrand,ProductAttributes, ProductImages, ProductAttributeValue, Product

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


# @admin.register(ProductImages)
# class ProductImagesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product', 'full_url', 'title', 'is_enabled', 'is_default', 'order_by', 'created')
#     search_fields = ('title', 'caption', 'product__name')
#     list_filter = ('is_enabled', 'is_default', 'created')
#     ordering = ('order_by', 'id')  # Order by the `order_by` field and ID
#     list_editable = ('is_enabled', 'is_default', 'order_by')  # Allow inline editing
#     readonly_fields = ('created',)  # Prevent editing the auto-updated `created` field

@admin.register(ProductAttributes)
class ProductAttributesAdmin(admin.ModelAdmin):
    """Customize the ProductAttributes admin interface."""
    list_display = ('id', 'attribute_name', 'is_default')
    list_filter = ('is_default',)  # Filter by default status
    search_fields = ('attribute_name',)  # Enable search by attribute name
    ordering = ('id',)  # Order by ID

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1  # Default number of empty forms in the inline section

class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'is_enabled', 'is_best_seller', 'is_home_featured', 'created', 'updated')
    search_fields = ('name', 'slug', 'category__name', 'brand__name')
    list_filter = ('is_enabled', 'is_best_seller', 'is_home_featured')
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from product name
    inlines = [ProductImagesInline, ProductAttributeValueInline]  # Add inlines for related models
    readonly_fields = ('created', 'updated')  # Make created and updated fields read-only
    fields = ('name', 'slug', 'brand', 'category', 'short_description', 'description', 'canonical_url', 'is_enabled', 'is_best_seller', 'is_home_featured', 'is_featured', 'created', 'updated', 'created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the product is being created, set the creator
            obj.created_by = request.user
        obj.updated_by = request.user  # Always set the updater
        super().save_model(request, obj, form, change)