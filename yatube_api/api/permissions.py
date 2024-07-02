from rest_framework import permissions

from rest_framework.response import Response
from rest_framework import status


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_authenticated:
            return False
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)


class ReadOnlyForGroup(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return request.method in permissions.SAFE_METHODS
    

class FollowPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        #if request.method == 'GET' and not request.user.is_authenticated:
        return False
    #    return request.user.is_authenticated
#
    #def has_object_permission(self, request, view, obj):
    #    return (obj.user == request.user
    #            or request.method in permissions.SAFE_METHODS)
