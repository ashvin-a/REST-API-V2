from .permissions import IsStaffEditorPermission  # ? This mixin is broken bro
from rest_framework import permissions


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQueryMixin:
    """
    This mixin validates whether the user is authenticated
    """

    user_field = "user"
    allowed_staff_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        if self.allowed_staff_view and user.is_staff:
            return qs.filter(**lookup_data)
        return qs.filter(**lookup_data)  # The most important line 🛐
