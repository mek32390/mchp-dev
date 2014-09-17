from django import template

from notification.models import Inbox,NotificationArchive
register = template.Library()

@register.inclusion_tag("notification/unread_notifications.html", takes_context=True)
def unread_notifications(context, num=10):
    if "user" in context:
        user = context["user"]
        if user.is_authenticated():
            messages = Inbox.notifications.list(user)
            return {
                "notifications": messages[:num],
            }

@register.assignment_tag(takes_context=True)
def unread_count(context):
    if "user" in context:
        user = context["user"]
        if user.is_authenticated():
            return Inbox.notifications.count(user)

@register.assignment_tag(takes_context=True)
def read_count(context):
    if "user" in context:
        user = context["user"]
        if user.is_authenticated():
            return NotificationArchive.notifications.count(user)

@register.inclusion_tag("notification/read_notifications.html", takes_context=True)
def read_notifications(context, unread=0):
    if "user" in context:
        if unread > 5 :
            return {
                'notifications': []
            }
        num = 5 - unread
        user = context["user"]
        if user.is_authenticated():
            return {
                'notifications': NotificationArchive.notifications.list(user, num=num)
            }

@register.inclusion_tag("notification/notifications_list.html", takes_context=True)
def notification_archive(context):
    if "user" in context:
        user = context["user"]
        if user.is_authenticated():
            # return 100 most recent 
            notifications = NotificationArchive.notifications.list(user, num=100)
            return {
                'notifications': notifications 
            }

