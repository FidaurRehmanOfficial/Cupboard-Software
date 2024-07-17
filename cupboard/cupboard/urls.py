"""
URL configuration for cupboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from business import views

urlpatterns = [
    path("admin/", admin.site.urls),
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
