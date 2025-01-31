from django import forms
from catalog.models import Product, ProductAttributes, ProductImages, ProductAttributeValue

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields = ['full_url', 'title', 'is_default']
        widgets = {
            'full_url': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'is_default': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

ProductImageFormSet = forms.modelformset_factory(
    ProductImages,
    form=ProductImageForm,
    extra=1,  # One empty form will always be rendered
    # can_delete=True  # Allow removing images dynamically
)

class ProductAttributeValueForm(forms.ModelForm):
    class Meta:
        model = ProductAttributeValue
        fields = ['attribute', 'attribute_value', 'order_no']
        widgets = {
            'attribute': forms.Select(attrs={'class': 'form-control'}),
            'attribute_value': forms.TextInput(attrs={'class': 'form-control'}),
            'order_no': forms.NumberInput(attrs={'class': 'form-control'}),
        }

ProductAttributeValueFormSet = forms.modelformset_factory(
    ProductAttributeValue,
    form=ProductAttributeValueForm,
    extra=1,  # Start with one empty form
    # can_delete=True  # Allow removal of extra forms
)

class ProductForm(forms.ModelForm):
    """
    Form for creating and updating a Product with attributes and attribute values.
    """
    
    other_brand = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type brand name', 'style': 'display:none;'}),
        label=""
    )
    class Meta:
        model = Product
        fields = [
            'name', 'brand', 'other_brand', 'category', 'short_description', 'description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'placeholder': 'Enter a brief description'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Enter a detailed description'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        brand = cleaned_data.get('brand')
        other_brand = cleaned_data.get('other_brand')
        
        # If the user selected "Other", ensure that other_brand is not empty
        if brand == '3' and not other_brand:
            raise forms.ValidationError("Please provide a custom brand name.")

        # If the user typed a custom brand, save it
        if brand == '3' and other_brand:
            cleaned_data['other_brand'] = other_brand.strip()


        return cleaned_data
