from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseForbidden

class RoleRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        # Define role-based access for different paths
        role_paths = {
            'admin': [
                '/admin_dashboard/',
                # Add other admin paths here
            ],
            'shopkeeper': [
                '/shopkeeper_dashboard/',
                '/inventory/',
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

        return HttpResponseForbidden("You do not have permission to view this page.")
