from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'company_name', 'barcode', 'address', 'zip_code', 'city', 'country',
            'contact_first_name', 'contact_last_name', 'title',
            'primary_phone_number', 'secondary_phone_number',
            'email_address', 'fax_address'
        ]
        widgets = {
            field: forms.TextInput(attrs={
                'class': 'form-control'
            })
            for field in fields
        }