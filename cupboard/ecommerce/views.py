from django.shortcuts import render
from .decorators import role_required

# Create your views here.

@role_required(['shopkeeper','admin'])
def shopkeeper_home(request):
    return render(request, 'ecommerce/index_for_shopkeeper.html')