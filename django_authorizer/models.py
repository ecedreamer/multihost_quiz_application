from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


User = get_user_model()

class Feature(models.Model):
    title = models.CharField(max_length=200)
    groups = models.ManyToManyField(Group)




class UserFeaturePermission(models.Model):
    feature = models.ManyToManyField(Feature)
    user = models.ForeignKey(User, on_delete=models.CASCADE)