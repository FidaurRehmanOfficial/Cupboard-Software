from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/create/', views.create_invoice, name='create_invoice'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/create/', views.create_inventory_item, name='create_inventory_item'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/create/', views.create_expense, name='create_expense'),
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/create/', views.create_payment, name='create_payment'),
    path('reports/profit-and-loss/', views.profit_and_loss_report, name='profit_and_loss_report'),
]
