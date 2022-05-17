
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


User = get_user_model()


class DevAdminBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(
                email=username, is_staff=True, is_superuser=True)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class EmailBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        email = kwargs.get("email")
        password = kwargs.get("password")
        try:
            user = User.objects.get(email=email, is_staff=False)
            if user.check_password(password):
                return user
            else:
                # need to include logging
                print("Password check false or is_staff false")
        except User.DoesNotExist:
            # need to include logging
            print("User does not exists")

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

