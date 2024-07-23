from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('invoices/', views.manage_invoices, name='manage_invoices'),
    path('invoices/new/', views.create_invoice, name='create_invoice'),
    path('invoices/<int:pk>/edit/', views.edit_invoice, name='edit_invoice'),
    path('invoices/<int:pk>/delete/', views.delete_invoice, name='delete_invoice'),
    path('inventory/', views.manage_inventory, name='manage_inventory'),
    path('inventory/new/', views.add_product, name='add_product'),
    path('inventory/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('inventory/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('expenses/', views.manage_expenses, name='manage_expenses'),
    path('expenses/new/', views.add_expense, name='add_expense'),
    path('expenses/<int:pk>/edit/', views.edit_expense, name='edit_expense'),
    path('expenses/<int:pk>/delete/', views.delete_expense, name='delete_expense'),
    path('reports/', views.reports, name='reports'),
    path('gst_reports/', views.manage_gst_reports, name='manage_gst_reports'),
    path('payments/', views.manage_payments, name='manage_payments'),
    path('payments/new/', views.add_payment, name='add_payment'),
    path('payments/<int:pk>/edit/', views.edit_payment, name='edit_payment'),
    path('payments/<int:pk>/delete/', views.delete_payment, name='delete_payment'),
]