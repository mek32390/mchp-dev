from django import template

from stored_messages.models import Inbox, MessageArchive
register = template.Library()

@register.inclusion_tag("notifications/unread_notifications.html", takes_context=True)
def unread_notifications(context, num=10):
    if "user" in context:
        user = context["user"]
        if user.is_authenticated():
            messages = Inbox.objects.select_related("message").filter(user=user).order_by('-message__date')
            return {
                "messages": messages[:num],
            }

@register.assignment_tag(takes_context=True)
def unread_count(context):
    if "user" in context:
        user = context["user"]
        if user.is_authenticated():
            return Inbox.objects.select_related("message").filter(user=user).count()

@register.assignment_tag(takes_context=True)
def read_count(context):
    if "user" in context:
        user = context["user"]
        if user.is_authenticated():
            return MessageArchive.objects.select_related("message").filter(user=user).count()

@register.inclusion_tag("notifications/read_notifications.html", takes_context=True)
def read_notifications(context, unread=0):
    if "user" in context:
        num = 5 - unread
        user = context["user"]
        if user.is_authenticated():
            qs = MessageArchive.objects.select_related("message").filter(user=user).order_by('-message__date')
            return {
                "messages": qs[unread:num+unread],
            }
