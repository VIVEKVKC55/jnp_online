from django.shortcuts import render
from catalog.models import Product, ProductImages

def home(request):
    # Fetch all products with their associated categories
    featured_products = Product.objects.filter(is_deleted=False, is_home_featured=True, is_enabled=True).order_by('-created')

    products = Product.objects.filter(is_deleted=False, is_enabled=True, is_approved=True).order_by('-created')
    
    context = {
        'products': products,
       'featured_products': featured_products
    }
    return render(request, 'default/home/index.html', context)