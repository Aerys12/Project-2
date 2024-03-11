from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `creator`.
        return obj.calendar.creator == request.user