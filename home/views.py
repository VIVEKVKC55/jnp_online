from django.shortcuts import render
from catalog.models import Product, ProductImages

def home(request):
    # Fetch all products with their associated categories
    products = Product.objects.filter(is_deleted=False, is_enabled=True).order_by('-created')
    featured_products = Product.objects.filter(is_deleted=False, is_home_featured=True, is_enabled=True).order_by('-created')

    # Fetch the first image for each product
    # products_with_details = []
    # for product in products:

    #     products_with_details.append({
    #         'product': product,
    #     })
    context = {
        'products': products,
       'featured_products': featured_products
    }
    return render(request, 'default/home/index.html', context)