from django.db import models
from core.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Invoice {self.id} - {self.customer.name}'
class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField()
    category = models.CharField(max_length=255)
    warehouse = models.CharField(max_length=255)
    batch_number = models.CharField(max_length=50)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name
class Expense(models.Model):
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)

    def __str__(self):
        return f'{self.category} - {self.amount}'
class GSTInvoice(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    gst_number = models.CharField(max_length=15)
    gst_rate = models.DecimalField(max_digits=5, decimal_places=2)
    gst_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'GST Invoice {self.invoice.id}'
class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    mode = models.CharField(max_length=50)

    def __str__(self):
        return f'Payment {self.id} - {self.amount}'
