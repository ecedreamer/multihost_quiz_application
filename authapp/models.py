from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy

# Admin User


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError(gettext_lazy("Superuser must be set staff=True"))
        if other_fields.get("is_superuser") is not True:
            raise ValueError(gettext_lazy(
                "Superuser must be set superuser=Trues"))
        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, *other_arg_fields, **other_kw_fields):
        if not email:
            raise ValueError(gettext_lazy("You must provide an email"))
        email = self.normalize_email(email)
        user = self.model(email=email, *other_arg_fields, **other_kw_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy('email address'), unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="users/", null=True, blank=True)
    mobile_number = models.CharField(max_length=10, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class HostUser(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.user.email


class ParticipantUser(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    host_group = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="participants")

    def __str__(self) -> str:
        return self.user.email
