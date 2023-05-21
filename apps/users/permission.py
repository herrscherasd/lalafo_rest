from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.pk == request.user.pk)