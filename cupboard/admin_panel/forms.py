from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['Customer', 'due_date', 'total_amount', 'is_paid']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'quantity', 'category', 'warehouse', 'batch_number', 'expiry_date']
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'date', 'description', 'receipt']
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['Customer', 'amount', 'date', 'mode']
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'contact', 'address', 'email']
class CustomerForm(forms.ModelForm):
    contact = models.CharField(max_length=100)
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address', 'email']        

""" class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('role',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields """