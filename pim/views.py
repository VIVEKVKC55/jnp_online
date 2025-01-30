from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product, ProductImages, ProductAttributeValue, ProductAttributes
from business.models import BusinessDetails
from .forms import ProductForm, ProductImageFormSet, ProductAttributeValueFormSet

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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'default/pim/add.html'
    success_url = reverse_lazy('pim:product_list')

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
        product_image_formset = ProductImageFormSet(queryset=ProductImages.objects.none())
        product_attribute_value_formset = ProductAttributeValueFormSet(queryset=ProductAttributeValue.objects.none())
        return self.render_to_response({
            'form': form, 
            'product_image_formset': product_image_formset,
            'product_attribute_value_formset': product_attribute_value_formset
        })
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # product_attribute_value_formset = ProductAttributeValueFormSet(request.POST)
        product_image_formset = ProductImageFormSet(request.POST, request.FILES)
        # product_attribute_value_formset.is_valid() and
        if form.is_valid() and product_image_formset.is_valid():
            # Save the main product form
            product = form.save(commit=False)
            product.created_by = self.request.user
            product.save()

            # Save all the valid product attribute value forms
            # for attribute_form in product_attribute_value_formset:
            #     if attribute_form.cleaned_data.get('attribute_value'):
            #         attribute_value = attribute_form.save(commit=False)
            #         attribute_value.product = product
            #         attribute_value.save()

            # Save all the valid product image forms
            for image_form in product_image_formset:
                if image_form.cleaned_data.get('full_url'):
                    image = image_form.save(commit=False)
                    image.product = product
                    image.save()

            return redirect(self.success_url)

        return self.render_to_response({
            'form': form,
            'product_image_formset': product_image_formset,
            # 'product_attribute_value_formset': product_attribute_value_formset,
        })
