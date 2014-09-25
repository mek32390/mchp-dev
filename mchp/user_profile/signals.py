from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User

from allauth.account.signals import user_logged_in

from notification.api import add_notification_for

@receiver(user_logged_in)
def log_in_notify(sender, request, user, **kwargs):
    adapt = User.objects.filter(
        username = 'Adapt',
    )
    mitch = User.objects.filter(
        username = 'mitchellias',
    )
    if adapt.exists():
        adapt = adapt[0]
    if mitch.exists():
        mitch = mitch[0]
    if not mitch and not adapt:
        return
    add_notification_for(
        [adapt, mitch],
        user.username + ' has logged in'
    )
