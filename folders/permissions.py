from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    # def has_permission(self, request, view):
    #     if view.action == "list":
    #         return request.user.is_staff
    #     elif view.action == "create":
    #         return True
    #     elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
    #         return True
    #     else:
    #         return False
        
    def has_object_permission(self, request, view, obj):
        if obj.profile.user == request.user:
            return True
        return False