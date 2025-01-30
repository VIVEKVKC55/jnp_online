from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product, ProductImages, ProductAttributeValue, ProductAttributes
from .forms import ProductForm, ProductImageFormSet

class ProductListView(LoginRequiredMixin, ListView):
    """
    View to list all products for the logged-in user.
    """
    model = Product
    template_name = 'default/pim/product_list.html'  # Update this to match your template
    context_object_name = 'products'
    paginate_by = 10  # Adjust pagination as needed

    def get_queryset(self):
        """
        Customize the queryset to return only products created by the current user.
        """
        return Product.objects.filter(created_by=self.request.user).select_related('category').order_by('name')


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
        if not hasattr(request.user, 'businessdetails'):
            # Redirect to a page or show an error if not a business user
            return redirect('home:home')  # Replace with actual page, e.g., login, or an error page
        
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Handle GET request to show the form.
        """
        form = self.get_form()
        product_image_formset = ProductImageFormSet(queryset=ProductImages.objects.none())  # Empty queryset for formset
        return self.render_to_response({'form': form, 'product_image_formset': product_image_formset})

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to save the form and formset data.
        """
        form = self.get_form()
        product_image_formset = ProductImageFormSet(request.POST, request.FILES)

        if form.is_valid() and product_image_formset.is_valid():
            # Save the product object but don't commit to the database yet
            product = form.save(commit=False)
            product.created_by = self.request.user
            product.save()

            # Save all the images
            for image_form in product_image_formset:
                if image_form.cleaned_data.get('full_url'):
                    image = image_form.save(commit=False)
                    image.product = product
                    image.save()

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

            return redirect(self.success_url)

        return self.render_to_response({'form': form, 'product_image_formset': product_image_formset})

    def form_valid(self, form):
        """
        The form has been validated, now save the product and the associated images and attributes.
        """
        # Product will be saved in the post method, so we don't need to save here again.
        return super().form_valid(form)
