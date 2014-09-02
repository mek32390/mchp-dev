from django.db import models

import notification.models

class InboxManager(models.Manager):
    def list(self, user, *args, **kwargs):
        num = kwargs.get('num', None)
        notifications = notification.models.Inbox.notifications.select_related(
            "notification"
        ).filter(
            user=user
        ).order_by('-notification__create_date')
        notifications = list(map(lambda notif: notif.notification, notifications))

        if num:
            return notifications[:num]
        else:
            return notifications

    def count(self, user):
        return notification.models.Inbox.notifications.filter(
            user=user
        ).count()

    def store(self, user, notif):
        notification.models.Inbox.notifications.create(
            user=user,
            notification=notif
        )

    def mark_all_read(self, user):
        notifs = notification.models.Inbox.notifications.filter(
            user=user
        )
        notifs = list(map(lambda notif: notif.notification, notifs))
        for notif in notifs:
            self.mark_read(user, notif)

    def mark_read(self, user, notif):
        # add to archive 
        notification.models.NotificationArchive.notifications.create(
            user=user,
            notification=notif
        )
        # delete from inbox
        notification.models.Inbox.notifications.filter(
            user=user,
            notification=notif
        ).delete()

class NotificationArchiveManager(models.Manager):
    def list(self, user, *args, **kwargs):
        num = kwargs.get('num', None)
        notifications = notification.models.NotificationArchive.notifications.select_related(
            "notification"
        ).filter(
            user=user
        ).order_by('-notification__create_date')
        notifications = list(map(lambda notif: notif.notification, notifications))

        if num:
            return notifications[:num]
        else:
            return notifications

    def count(self, user):
        return notification.models.NotificationArchive.notifications.filter(
            user=user
        ).count()


