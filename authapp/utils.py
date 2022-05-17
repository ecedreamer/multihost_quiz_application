from .models import HostUser, ParticipantUser


def check_host(user):
    if HostUser.objects.filter(user=user).exists():
        return HostUser.objects.get(user=user)
    return None

def check_participant(user):
    if ParticipantUser.objects.filter(user=user).exists():
        return ParticipantUser.objects.get(user=user)
    return None

    