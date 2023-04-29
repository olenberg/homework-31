from rest_framework.permissions import BasePermission


class IsOwnerOrAdminOrModerator(BasePermission):
    message = "Only the owner, administrator, or moderator can edit or delete an ad."

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user or request.user.role in ["admin", "moderator"]:
            return True
