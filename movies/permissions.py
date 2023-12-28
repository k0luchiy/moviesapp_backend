from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_staff

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_staff
        elif view.action == "create":
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_staff
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if obj.profile.user == request.user:
            return True
        return False

