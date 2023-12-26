from .permissions import IsStaffEditorPermission
from rest_framework import permissions


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQueryMixin:
    """
    This mixin validates whether the user is authenticated
    """

    user_field = "user"

    def get_queryset(self, *args, **kwargs):
        lookup = {}
        lookup["user"] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup)  # The most important line 🛐
