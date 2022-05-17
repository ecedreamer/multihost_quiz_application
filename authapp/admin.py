from django.contrib import admin
from .models import HostUser, ParticipantUser, User


admin.site.register([User, HostUser, ParticipantUser])