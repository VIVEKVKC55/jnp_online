from django.shortcuts import render
from catalog.models import Product, ProductImages

def home(request):
    # Fetch all products with their associated categories
    products = Product.objects.filter(is_deleted=False, is_enabled=True, is_approved=True).order_by('-created')
    
    context = {
        'products': products,
    }
    return render(request, 'default/home/index.html', context)