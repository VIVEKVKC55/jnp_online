from django import forms
from catalog.models import Product, ProductAttributes, ProductAttributeValue
from django.forms import ClearableFileInput


class MultiFileInput(ClearableFileInput):
    template_name = 'django/forms/widgets/clearable_file_input.html'

    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = kwargs.get('attrs', {})
        kwargs['attrs']['multiple'] = 'multiple'
        super().__init__(*args, **kwargs)

class ProductForm(forms.ModelForm):
    """
    Form for creating and updating a Product with attributes and attribute values.
    """
    attributes_with_values = forms.ModelMultipleChoiceField(
        queryset=ProductAttributes.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select Attributes"
    )
    
    attribute_values = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter corresponding attribute values'}),
        required=False,
        label="Enter Attribute Values"
    )
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': False}),
        required=False,  # Optional; you can make it required if needed
        label="Upload Images"
    )
    class Meta:
        model = Product
        fields = [
            'name', 'brand', 'category', 'short_description',
            'description', 'canonical_url', 'is_best_seller',
            'is_home_featured', 'is_featured', 'is_enabled',
            'images',
        ]

    def clean(self):
        cleaned_data = super().clean()
        attribute_values = cleaned_data.get("attribute_values")
        attributes = cleaned_data.get("attributes_with_values")

        # Ensure that each attribute has a corresponding value
        if attributes and not attribute_values:
            raise forms.ValidationError("Please provide attribute values for the selected attributes.")

        return cleaned_data
