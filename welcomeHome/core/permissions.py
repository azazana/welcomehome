from rest_framework import permissions


class CustomDeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != 'GET':
            return False
        return True
