from django.dispatch import Signal
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User

from allauth.account.signals import user_logged_in

from notification.api import add_notification

enrolled = Signal(providing_args=['enroll'])

@receiver(user_logged_in)
def log_in_notify(sender, request, user, **kwargs):
    me = User.objects.filter(
        username = 'Adapt',
    )
    if me.exists():
        me = me[0]
    else:
        return
    add_notification(
        me,
        user.username + ' has logged in'
    )
