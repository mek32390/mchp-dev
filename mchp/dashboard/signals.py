from django.dispatch.dispatcher import receiver

from calendar_mchp.signals import calendar_event_created
from dashboard.models import DashEvent
from dashboard.utils import DASH_EVENTS

@receiver(calendar_event_created)
def create_event(sender, **kwargs):
    event = kwargs['event']

    calendar = event.calendar
    followers = calendar.subscribers.all()
    data = {
        'type': DASH_EVENTS.index('calendar add'),
        'calendar': calendar,
        'course': calendar.course,
        'student': calendar.owner,
    }
    dash = DashEvent(**data)
    dash.event = event
    dash.save()
    for student in followers:
        dash.followers.add(student)
