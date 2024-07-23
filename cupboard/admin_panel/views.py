from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

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
def manage_expenses(request):
    expenses = Expense.objects.all()
    return render(request, 'admin_panel/manage_expenses.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'admin_panel/expense_form.html', {'form': form})

def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('manage_expenses')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'admin_panel/expense_form.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('manage_expenses')
def reports(request):
    return render(request, 'admin_panel/reports.html')
def manage_gst_reports(request):
    gst_invoices = GSTInvoice.objects.all()
    return render(request, 'admin_panel/manage_gst_reports.html', {'gst_invoices': gst_invoices})
def manage_payments(request):
    payments = Payment.objects.all()
    return render(request, 'admin_panel/manage_payments.html', {'payments': payments})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_payments')
    else:
        form = PaymentForm()
    return render(request, 'admin_panel/payment_form.html', {'form': form})

def edit_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('manage_payments')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'admin_panel/payment_form.html', {'form': form})

def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    payment.delete()
    return redirect('manage_payments')
