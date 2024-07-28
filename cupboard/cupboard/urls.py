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
from django.urls import path, include
from business.views import index
from django.contrib.auth import views as auth_views
from admin_panel.views import *
from core.views import RoleBasedLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('index/', index, name='index'),
    path('business/', include('business.urls')),
    path('', include('ecommerce.urls'), name='shopkeeper_dashboard'),
    path('admin-panel/', include('admin_panel.urls')),
    path('login/', RoleBasedLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
