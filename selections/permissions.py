from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Only the owner, can edit or delete an selection."

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
