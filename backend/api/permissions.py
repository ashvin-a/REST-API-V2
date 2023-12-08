from rest_framework.permissions import DjangoModelPermissions

class IsStaffEditorPermission(DjangoModelPermissions):
    """
    This is the class that
    """
    perms_map = {
        'OPTIONS': [],
        'HEAD': [],
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
    }
    
    # def has_permission(self, request, view):
    #     user = request.user
    #     if not user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
