from django.shortcuts import render, redirect
from .models import Invoice, InventoryItem, Expense, Payment
from .forms import InvoiceForm, InventoryItemForm, ExpenseForm, PaymentForm
from django.db.models import Sum

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
def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'business/create_expense.html', {'form': form})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'business/expense_list.html', {'expenses': expenses})

def profit_and_loss_report(request):
    total_income = Invoice.objects.aggregate(Sum('total_amount'))['total_amount__sum']
    total_expenses = Expense.objects.aggregate(Sum('amount'))['amount__sum']
    profit_or_loss = total_income - total_expenses
    return render(request, 'business/profit_and_loss_report.html', {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'profit_or_loss': profit_or_loss
    })
def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'business/create_payment.html', {'form': form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'business/payment_list.html', {'payments': payments})