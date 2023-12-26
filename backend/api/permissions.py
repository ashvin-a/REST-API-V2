from rest_framework.permissions import DjangoModelPermissions


class IsStaffEditorPermission(DjangoModelPermissions):
    """
    This is the class that
    """

    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

    # def has_permission(self, request, view):
    #     user = request.user
    #     if not user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
