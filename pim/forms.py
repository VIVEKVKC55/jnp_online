from django import forms
from catalog.models import Product, ProductAttributes, ProductAttributeValue


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
            'placeholder': 'Enter corresponding attribute values',
            'class': 'form-control',
            'rows': 3
        }),
        required=False,
        label="Enter Attribute Values"
    )
    
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'multiple': False
        }),
        required=False,  # Optional; you can make it required if needed
        label="Upload Images"
    )
    class Meta:
        model = Product
        fields = [
            'name', 'brand', 'category', 'short_description',
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

        # Ensure that each attribute has a corresponding value
        if attributes and not attribute_values:
            raise forms.ValidationError("Please provide attribute values for the selected attributes.")

        return cleaned_data
