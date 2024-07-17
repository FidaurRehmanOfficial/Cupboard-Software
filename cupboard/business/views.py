from django.shortcuts import render, redirect
from .models import Invoice, InventoryItem
from .forms import InvoiceForm, InventoryItemForm

# Create your views here.

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'business/create_invoice.html', {'form': form})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'business/invoice_list.html', {'invoices': invoices})
def create_inventory_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    return render(request, 'business/create_inventory_item.html', {'form': form})

def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'business/inventory_list.html', {'items': items})