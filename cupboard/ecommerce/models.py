from django.db import models
from django.urls import path
from . import views

# Create your models here.
urlpatterns = [
    path('', views.shopkeeper_home, name='shopkeeper_home'),
]