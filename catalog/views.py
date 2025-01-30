from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImages, ProductAttributeValue
from business.models import BusinessDetails

def product_detail(request, pk):
    # Fetch the product by pk
    product = get_object_or_404(Product, id=pk, is_deleted=False, is_enabled=True)
    images = ProductImages.objects.filter(product=product, is_enabled=True).order_by('order_by')
    attributes = ProductAttributeValue.objects.filter(product=product)

    businuss_details = BusinessDetails.objects.get(user=product.created_by)

    context = {
        'product': product,
        'images': images,
        'attributes': attributes,
        'businuss_details': businuss_details,
    }
    return render(request, 'default/catalog/product.html', context)

def product_list(request):
    products = Product.objects.filter(is_deleted=False, is_enabled=True)
    return render(request, 'default/catalog/product_list.html', {'products': products})

