from django.contrib import admin
from .models import *

# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('customer_name',  'invoice_date', 'due_date', 'total_amount', 'paid') # 'customer_email',
    search_fields = ('customer_name', 'invoice_date') # , 'customer_email'
    list_filter = ('paid', 'invoice_date')

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'purchase_price', 'selling_price')
    search_fields = ('name',)
    list_filter = ('quantity',)

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date')
    search_fields = ('description',)
    list_filter = ('date',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount', 'payment_date', 'method')
    search_fields = ('invoice__customer_name', 'method')
    list_filter = ('payment_date', 'method')
#class InvoiceAdmin(admin.ModelAdmin):
#    list_display = ('customer_name', 'invoice_date', 'due_date', 'total_amount', 'paid')
#    search_fields = ('customer_name', )
#    list_filter = ('paid', 'invoice_date')
#    fieldsets = (
#        (None, {
#            'fields': ('customer_name', 'due_date', 'total_amount', 'paid')
#        }),
#        ('Dates', {
#            'fields': ('invoice_date',),
#        }),
#    )


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InventoryItem, InventoryItemAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Payment, PaymentAdmin)