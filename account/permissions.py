from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access certain views.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_admin

class IsRegularUser(permissions.BasePermission):
    """
    Custom permission to only allow regular users to access certain views.
    """
    def has_permission(self, request, view):
        return request.user and not request.user.is_admin
