from django import forms
from .models import Invoice, Product

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer', 'due_date', 'total_amount', 'is_paid']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'quantity', 'category', 'warehouse', 'batch_number', 'expiry_date']
