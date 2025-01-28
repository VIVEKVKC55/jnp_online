from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImages, ProductAttributeValue

def product_detail(request, pk):
    # Fetch the product by slug
    product = get_object_or_404(Product, id=pk, is_deleted=False, is_enabled=True)
    
    # Fetch associated images
    images = ProductImages.objects.filter(product=product, is_enabled=True).order_by('order_by')

    # Fetch related attributes and their values
    attributes = ProductAttributeValue.objects.filter(product=product)

    # Pass the product, images, and attributes to the template
    context = {
        'product': product,
        'images': images,
        'attributes': attributes,
    }
    return render(request, 'default/catalog/product.html', context)

def product_list(request):
    products = Product.objects.filter(is_deleted=False, is_enabled=True)
    return render(request, 'default/catalog/product_list.html', {'products': products})

