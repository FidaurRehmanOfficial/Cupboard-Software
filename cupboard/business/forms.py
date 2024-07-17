from django import forms
from .models import Invoice, InventoryItem

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name', 'customer_email', 'due_date', 'total_amount']
class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'purchase_price', 'selling_price']