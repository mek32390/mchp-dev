from notification.models import Notification, Inbox

def add_notification(user, message):
    notification = Notification.objects.create(message=message)
    Inbox.notifications.store(user,notification)

def add_notification_for(users, message):
    notification = Notification.objects.create(message=message)
    for user in users:
        Inbox.notifications.store(user,notification)

def mark_read(user, notification):
    Inbox.notifications.mark_read(user)

def mark_all_read(user):
    Inbox.notifications.mark_all_read(user)
