from rest_framework.permissions import BasePermission
from auth import logger

class IsModerator(BasePermission):
    '''
    Allows access only to moderators and superusers.
    '''

    def has_permission(self, request, view):
        logger.info('Checking if user has moderator access.')
        is_true = (
            request.user.user_type == "moderator" 
            or request.user.is_staff
            or request.user.is_superuser
        )
        return bool(is_true and request.user.is_authenticated)