from django.shortcuts import render

# Create your views here.

def shopkeeper_home(request):
    return render(request, 'ecommerce/index_for_shopkeeper.html')