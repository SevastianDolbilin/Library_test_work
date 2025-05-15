from rest_framework import permissions


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Кастовое разрешение.
    Доступ на запись только для суперпользователей, чтение открыто всем.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser
