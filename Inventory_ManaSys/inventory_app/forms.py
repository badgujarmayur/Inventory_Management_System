from django import forms
from .models import Inventory

class InventoryInfoForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'  # Use 'fields' instead of 'field'
        labels = {
            "material": "Materials",
            "price": "Price",
            "city": "City",
            "parent_company": "Parent Company"  # Use space instead of underscore for label
        }
        widgets = {  # Change from parentheses to curly braces
            'material': forms.TextInput(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'city': forms.TextInput(attrs={"class": "form-control"}),
            'parent_company': forms.Select(attrs={"class": "form-control"})
        }
