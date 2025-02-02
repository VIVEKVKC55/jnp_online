from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import View, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product, ProductImages, ProductAttributeValue
from business.models import BusinessDetails
from .forms import (
    ProductForm, 
    ProductImageUpdateFormSet, 
    ProductImageFormSet, 
    ProductAttributeValueFormSet, 
    ProductAttributeValueUpdateFormSet
    )

class ProductListView(LoginRequiredMixin, ListView):
    """
    View to list all products for the logged-in user.
    """
    model = Product
    template_name = 'default/pim/list.html'  # Update this to match your template
    context_object_name = 'products'
    paginate_by = 10  # Adjust pagination as needed

    def get_queryset(self):
        """
        Customize the queryset to return only products created by the current user.
        """
        return Product.objects.filter(created_by=self.request.user).select_related('category').order_by('-id')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'default/pim/add.html'
    success_url = reverse_lazy('pim:list')

    def get(self, request, *args, **kwargs):
        try:
            business_details = BusinessDetails.objects.get(user=request.user)
            if not business_details.is_approved:
                messages.error(request, "Your business details have not been approved.")
                return redirect('home:home')
        except BusinessDetails.DoesNotExist:
            messages.error(request, "You must have business details to access this page.")
            return redirect('home:home')

        form = self.get_form()
        product_image_formset = ProductImageFormSet(queryset=ProductImages.objects.none(), prefix='images')
        product_attribute_value_formset = ProductAttributeValueFormSet(queryset=ProductAttributeValue.objects.none(), prefix='attributes')

        return self.render_to_response({
            'form': form,
            'product_image_formset': product_image_formset,
            'product_attribute_value_formset': product_attribute_value_formset
        })

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        product_image_formset = ProductImageFormSet(request.POST, request.FILES, prefix='images')
        product_attribute_value_formset = ProductAttributeValueFormSet(request.POST, prefix='attributes')

        if form.is_valid() and product_image_formset.is_valid() and product_attribute_value_formset.is_valid():
            # Save the product first
            product = form.save(commit=False)
            product.created_by = self.request.user
            product.save()

            # Save product images
            for image_form in product_image_formset:
                print('image_form',image_form.changed_data)
                if image_form.cleaned_data.get('full_url'):  # Ensure there's an image
                    image = image_form.save(commit=False)
                    image.product = product
                    image.save()

            # Save product attributes
            for attribute_form in product_attribute_value_formset:
                print('attribute_form',attribute_form.changed_data)
                if attribute_form.cleaned_data.get('attribute_value'):  # Ensure there's an attribute value
                    attribute_value = attribute_form.save(commit=False)
                    attribute_value.product = product
                    attribute_value.save()

            return redirect(self.success_url)

        # If validation fails, re-render the form
        return self.render_to_response({
            'form': form,
            'product_image_formset': product_image_formset,
            'product_attribute_value_formset': product_attribute_value_formset,
        })


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'default/pim/edit.html'
    success_url = reverse_lazy('pim:list')

    def dispatch(self, request, *args, **kwargs):
        """Restrict access if business details are missing or not approved."""
        try:
            business_details = BusinessDetails.objects.get(user=request.user)
            if not business_details.is_approved:
                messages.error(request, "Your business details have not been approved.")
                return redirect('home:home')
        except BusinessDetails.DoesNotExist:
            messages.error(request, "You must have business details to access this page.")
            return redirect('home:home')

        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """Fetch the product object using URL kwargs."""
        return get_object_or_404(Product, pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        product = self.get_object()  # Get the product instance
        form_class = self.get_form_class()  # Get the form class
        form = form_class(instance=product)  # Create form with instance data

        return self.render_to_response({
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        product = self.get_object()  # Fetch product instance
        form = self.get_form_class()(request.POST, request.FILES, instance=product)  # Create form with instance data

        if form.is_valid():
            # Save the product instance
            product = form.save(commit=False)
            product.save()
            messages.success(request, "Product updated successfully!")
            return redirect(self.success_url)
        else:
            # Debugging: Check the errors in formset and form
            print("Form errors:", form.errors)
        return self.render_to_response({
            'form': form,
        })



class ProductDeleteView(View):
    def post(self, request, *args, **kwargs):
        # Get the product to delete
        product = get_object_or_404(Product, pk=self.kwargs['pk'])

        # Delete the product
        product.delete()

        # Show a success message
        messages.success(request, f"Product '{product.name}' has been deleted successfully.")

        # Redirect to the product list page
        return redirect(reverse_lazy('pim:list'))

    def get(self, request, *args, **kwargs):
        # If someone tries to access the delete URL directly via GET, redirect them to the list view
        return redirect(reverse_lazy('pim:list'))


class ProductImageUpdateView(View):
    def get_object(self, queryset=None):
        """Fetch the product object using URL kwargs."""
        return get_object_or_404(Product, pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        product = self.get_object()  # Get the product instance
        
        product_image_formset = ProductImageUpdateFormSet(instance=product, prefix='images')

        if not product_image_formset.forms:
            product_image_formset = ProductImageFormSet(instance=product, prefix='images')

        return self.render_to_response(request, {
            'product': product,
            'product_image_formset': product_image_formset
        })

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Fetch product instance

        # Bind formset with POST data and files (No `queryset` filter)
        product_image_formset = ProductImageFormSet(
            request.POST, request.FILES, instance=self.object, prefix='images'
        )

        if product_image_formset.is_valid():
            # Save all images (existing + new)
            image_instances = product_image_formset.save(commit=False)

            # Save new images and associate with the product
            for image in image_instances:
                image.product = self.object  # Explicitly set the product
                image.save()  # Save to the database

            # Handle deletions
            for form in product_image_formset.deleted_objects:
                form.delete()  # Delete marked objects

            product_image_formset.save_m2m()  # Save many-to-many relationships (if any)

            messages.success(request, "Product images updated successfully!")
            return redirect('pim:edit', pk=self.object.id)
        else:
            messages.error(request, "There was an error with your image formset.")
        
        return self.render_to_response(request, {
            'product': self.object,
            'product_image_formset': product_image_formset
        })

    def render_to_response(self, request, context, **kwargs):
        """Render the response using the correct template and include the 'request' object."""
        return render(request, 'default/pim/edit_images.html', context)


class ProductAttributeUpdateView(View):
    def get_object(self, queryset=None):
        """Fetch the product object using URL kwargs."""
        return get_object_or_404(Product, pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        product = self.get_object()  # Get the product instance
        
        product_attribute_formset = ProductAttributeValueUpdateFormSet(instance=product, prefix='attributes')

        if not product_attribute_formset.forms:
            product_attribute_formset = ProductAttributeValueFormSet(instance=product, prefix='attributes')

        return self.render_to_response(request, {
            'product': product,
            'product_attribute_formset': product_attribute_formset
        })

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Fetch product instance

        # Bind formset with POST data and files (No `queryset` filter)
        product_attribute_formset = ProductAttributeValueFormSet(
            request.POST, request.FILES, instance=self.object, prefix='attributes'
        )

        if product_attribute_formset.is_valid():
            # Save all attributes (existing + new)
            attribute_instances = product_attribute_formset.save(commit=False)

            # Save new attributes and associate with the product
            for attribute in attribute_instances:
                attribute.product = self.object  # Explicitly set the product
                attribute.save()  # Save to the database

            # Handle deletions
            for form in product_attribute_formset.deleted_objects:
                form.delete()  # Delete marked objects

            product_attribute_formset.save_m2m()  # Save many-to-many relationships (if any)

            messages.success(request, "Product attributes updated successfully!")
            return redirect('pim:edit', pk=self.object.id)
        else:
            messages.error(request, "There was an error with your attribute formset.")
        
        return self.render_to_response(request, {
            'product': self.object,
            'product_attribute_formset': product_attribute_formset
        })

    def render_to_response(self, request, context, **kwargs):
        """Render the response using the correct template and include the 'request' object."""
        return render(request, 'default/pim/edit_attributes.html', context)