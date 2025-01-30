from django import forms
from catalog.models import Product, ProductAttributes, ProductImages

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields = ['full_url', 'title', 'order_by', 'is_default']
        widgets = {
            'full_url': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': False}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'order_by': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_default': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

ProductImageFormSet = forms.modelformset_factory(ProductImages, form=ProductImageForm, extra=1)

class ProductForm(forms.ModelForm):
    """
    Form for creating and updating a Product with attributes and attribute values.
    """
    attributes_with_values = forms.ModelMultipleChoiceField(
        queryset=ProductAttributes.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        }),
        required=False,
        label="Select Attributes"
    )
    
    attribute_values = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter corresponding attribute values (Separate by commas)',
            'class': 'form-control',
            'rows': 3
        }),
        required=False,
        label="Enter Attribute Values"
    )
    
    other_brand = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type brand name', 'style': 'display:none;'}),
        label=""
    )
    class Meta:
        model = Product
        fields = [
            'name', 'brand', 'other_brand', 'category', 'short_description',
            'description', 'is_enabled',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Enter a brief description'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter a detailed description'
            }),
            'is_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        attribute_values = cleaned_data.get("attribute_values")
        attributes = cleaned_data.get("attributes_with_values")
        brand = cleaned_data.get('brand')
        other_brand = cleaned_data.get('other_brand')
        
        # If the user selected "Other", ensure that other_brand is not empty
        if brand == '3' and not other_brand:
            raise forms.ValidationError("Please provide a custom brand name.")

        # If the user typed a custom brand, save it
        if brand == '3' and other_brand:
            cleaned_data['other_brand'] = other_brand.strip()

        # Ensure that each attribute has a corresponding value
        if attributes and not attribute_values:
            raise forms.ValidationError("Please provide attribute values for the selected attributes.")

        return cleaned_data
