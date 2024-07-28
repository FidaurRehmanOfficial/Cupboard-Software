from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView

# Create your views here.

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'admin'

class ShopkeeperRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'shopkeeper'

""" class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'manager' """

class AdminDashboardView(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'admin_panel/admin_dashboard.html'

class ShopkeeperDashboardView(LoginRequiredMixin, ShopkeeperRequiredMixin, TemplateView):
    template_name = '/index_for_shopkeeper.html'

""" class ManagerDashboardView(LoginRequiredMixin, ManagerRequiredMixin, TemplateView):
    template_name = 'admin_panel/manager_dashboard.html' """

class RoleBasedLoginView(LoginView):
    template_name = 'login.html'


    def get_success_url(self):
        user = self.request.user
        if user.role == 'admin':
            return '/admin_panel/'
        elif user.role == 'shopkeeper':
            return '/'
        else:
            return '/'
"""         elif user.role == 'manager':
            return '/manager_dashboard/' """