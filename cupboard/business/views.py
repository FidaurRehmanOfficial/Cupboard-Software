from django.shortcuts import render, redirect
from .models import Invoice
from .forms import InvoiceForm

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