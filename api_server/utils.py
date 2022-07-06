from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'success': True,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'email': user.email,
    }


class UserOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_active)