from rest_framework.permissions import BasePermission


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and request.user.is_employer
        return True