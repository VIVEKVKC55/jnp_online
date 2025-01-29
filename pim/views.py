from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product, ProductImages, ProductAttributeValue, ProductAttributes
from .forms import ProductForm


class ProductListView(LoginRequiredMixin,ListView):
    """
    View to list all products.
    """
    model = Product
    template_name = 'default/pim/product_list.html'  # Update this to match your template
    context_object_name = 'products'
    paginate_by = 10  # Adjust pagination as needed

    def get_queryset(self):
        """
        Customize the queryset if needed (e.g., filter by category, search, etc.).
        """
        return Product.objects.select_related('category').order_by('name')
    

class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new product, including associated images and product attributes.
    """
    model = Product
    form_class = ProductForm
    template_name = 'default/pim/add.html'
    success_url = reverse_lazy('pim:product_list')

    def dispatch(self, request, *args, **kwargs):
        """
        Restrict access to business users only.
        """
        # Check if the user is a business user by verifying if they have a BusinessRegistration
        if not hasattr(request.user, 'businessregistration'):
            # Redirect to a page or show an error if not a business user
            return redirect('home:home')  # Replace with actual page, e.g., login, or an error page
        
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Automatically set the created_by user, handle product images, attributes, and attribute values.
        """
        # Save the product object but don't commit to the database yet
        product = form.save(commit=False)
        product.created_by = self.request.user
        product.save()

        # Handle image uploads (if any)
        images = self.request.FILES.getlist('images')  # Get all uploaded images
        if images:
            for image in images:
                ProductImages.objects.create(
                    product=product,
                    full_url=image,
                    title=image.name,  # Optional: You can customize the title
                    is_enabled=True,
                    is_default=True if images.index(image) == 0 else False  # Make the first image default
                )

        # Handle selected attributes and their values
        attributes = form.cleaned_data.get('attributes_with_values')  # Get the selected attributes
        attribute_values = form.cleaned_data.get('attribute_values')  # Get the provided values for attributes

        if attributes and attribute_values:
            # Split the provided values by line breaks, assuming each line corresponds to a value for an attribute
            attribute_value_list = attribute_values.splitlines()

            for i, attribute in enumerate(attributes):
                # Check if there are enough attribute values provided
                if i < len(attribute_value_list):
                    # Save the attribute value in the ProductAttributeValue table
                    ProductAttributeValue.objects.create(
                        product=product,
                        attribute=attribute,
                        attribute_value=attribute_value_list[i]
                    )

        # Now that everything is handled, return the success response
        return super().form_valid(form)