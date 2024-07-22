from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopkeeper_home, name='shopkeeper_home'),
]