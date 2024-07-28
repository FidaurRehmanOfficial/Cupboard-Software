from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseForbidden

class RoleRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Allow access to the login page for unauthenticated users
        if not request.user.is_authenticated:
            if request.path != reverse('login'):
                return redirect('login')
            return None
        if request.path == reverse('logout'):
            return None

        # Define role-based access for different paths
        role_paths = {
            'admin': [
                '/',
                '/logout/',
                '/admin/',
                '/admin/logout/',
                '/admin/',
                '/admin/',
                '/admin_panel/',
                '/invoices/',
                '/invoices/new/',
                '/invoices/<int:pk>/edit/',
                '/invoices/<int:pk>/delete/',
                '/inventory/',
                '/inventory1/',
                '/inventory/new/',
                '/inventory/<int:pk>/edit/',
                '/inventory/<int:pk>/delete/',
                '/expenses/',
                '/expenses/new/',
                '/expenses/<int:pk>/edit/',
                '/expenses/<int:pk>/delete/',
                '/reports/',
                '/gst_reports/',
                '/payments/',
                '/payments/new/',
                '/payments/<int:pk>/edit/',
                '/payments/<int:pk>/delete/',
                '/settings/',
                '/vendors/',
                '/vendors/new/',
                '/vendors/<int:pk>/edit/',
                '/vendors/<int:pk>/delete/',
                '/parties',
                '/Customers/',
                '/Customers/new/',
                '/Customers/<int:pk>/edit/',
                '/Customers/<int:pk>/delete/',
                        
            ],
            'shopkeeper': [
                '/',
                '/logout/',
                # Add other shopkeeper paths here
            ],
            'manager': [
                '/manager_dashboard/',
                # Add other manager paths here
            ],
        }

        # Check if the user's role is allowed for the requested path
        for role, paths in role_paths.items():
            if request.user.role == role and request.path in paths:
                return None

        return HttpResponseForbidden(render(request, 'no_permission.html'))
