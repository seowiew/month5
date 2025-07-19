from rest_framework.permissions import BasePermission

class IsModeratorPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            if request.method == 'POST':
                return False
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True
