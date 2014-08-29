from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

from notification import managers

class Notification(models.Model):
    message = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message

class NotificationArchive(models.Model):
    user = models.ForeignKey(User, related_name='notification_archive')
    notification = models.ForeignKey(Notification)

    notifications = managers.NotificationArchiveManager()

    def __str__(self):
        return "[{}] {}".format(self.user, self.message)

class Inbox(models.Model):
    user = models.ForeignKey(User, related_name='notification_inbox')
    notification = models.ForeignKey(Notification)

    notifications = managers.InboxManager()

    class Meta:
        verbose_name_plural = ('inboxes')

    def expired(self):
        expiration_date = self.message.date + timezone.timedelta(
            days=settings.INBOX_EXPIRE_DAYS
        )
        return expiration_date <= timezone.now()
    expired.boolean = True # show a nifty icon in the admin

    def __str__(self):
        return "[{}] {}".format(self.user, self.notification)
