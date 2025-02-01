from rest_framework.permissions import BasePermission

# Custom permission
class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated and request.user.is_superuser
    
    # id based permission
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated and request.user.is_superuser