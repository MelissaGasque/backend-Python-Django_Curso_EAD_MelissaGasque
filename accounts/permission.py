from rest_framework import permissions
from rest_framework.views import Request, View


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.user.is_authenticated and request.user.is_superuser:
            return True


class IsSuperUserOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method == 'GET' and request.user.is_authenticated:
            return True
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False
