from rest_framework.permissions import BasePermission

class isRecuriter(BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            return False
        
        if not request.user.is_authenticated:
            return False
        
        if request.user.is_authenticated and request.user.user_type.lower() == 'post_job'.lower():
            return True

