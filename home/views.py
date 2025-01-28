from django.shortcuts import render
from catalog.models import Product, ProductImages

def home(request):
    # Fetch all products with their associated categories
    products = Product.objects.filter(is_deleted=False, is_enabled=True)

    # Fetch the first image for each product
    products_with_details = []
    for product in products:
        image = ProductImages.objects.filter(product=product, is_enabled=True).first()

        products_with_details.append({
            'product': product,
            'image': image,
        })
        print(products_with_details)
    context = {
        'products': products_with_details,
    }
    return render(request, 'default/home/index.html', context)