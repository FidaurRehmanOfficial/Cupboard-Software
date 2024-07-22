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
]