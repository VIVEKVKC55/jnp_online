from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ProductImages, ProductAttributeValue
from business.models import BusinessDetails
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

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

class CategoryProductView(ListView):
    model = Product
    template_name = 'default/catalog/cat_products.html'
    context_object_name = 'products'
    paginate_by = 10  # Optional: Add pagination

    def get_queryset(self):
        """Get products for a specific category."""
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category, is_enabled=True, is_deleted=False)

    def get_context_data(self, **kwargs):
        """Add category object to context."""
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context