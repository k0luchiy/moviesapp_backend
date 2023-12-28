from rest_framework.permissions import BasePermission


class CustomUserPremissions(BasePermission):

    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_authenticated and request.user.is_staff
        elif view.action == "create":
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj or request.user.is_staff:
            return True
        return False
