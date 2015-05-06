from django.db import models


class SubscriberManager(models.Manager):
    """ Return only subscribers with active user accounts. """
    def get_queryset(self):
        return super().get_queryset().filter(user__is_active=True)
