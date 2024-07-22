from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice, Product
from .forms import InvoiceForm, ProductForm

# Create your views here.
def admin_dashboard(request):
    return render(request, 'admin_panel/admin_dashboard.html')

def manage_invoices(request):
    return render(request, 'admin_panel/manage_invoices.html')
def manage_invoices(request):
    invoices = Invoice.objects.all()
    return render(request, 'admin_panel/manage_invoices.html', {'invoices': invoices})

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.created_by = request.user
            invoice.save()
            return redirect('manage_invoices')
    else:
        form = InvoiceForm()
    return render(request, 'admin_panel/invoice_form.html', {'form': form})

def edit_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('manage_invoices')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'admin_panel/invoice_form.html', {'form': form})

def delete_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    invoice.delete()
    return redirect('manage_invoices')
def manage_inventory(request):
    products = Product.objects.all()
    return render(request, 'admin_panel/manage_inventory.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_inventory')
    else:
        form = ProductForm()
    return render(request, 'admin_panel/product_form.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manage_inventory')
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin_panel/product_form.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('manage_inventory')