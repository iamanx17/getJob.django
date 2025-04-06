from rest_framework.permissions import BasePermission

class isApplicant(BasePermission):

    def has_permission(self, request, view):
        if not request.user:
            return False
        
        if not request.user.is_authenticated:
            return False
        
        if request.user.user_type.lower() == 'apply_job'.lower():
            return True
        
        return False