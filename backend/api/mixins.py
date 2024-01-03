from .permissions import IsStaffEditorPermission  # ? This mixin is broken bro
from rest_framework import permissions


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQueryMixin():
    """
    This mixin validates whether the user is authenticated
    """

    user_field = "user"

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup = {}
        lookup[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        if user.is_staff:
            return qs
        return qs.filter(**lookup)  # The most important line 🛐
