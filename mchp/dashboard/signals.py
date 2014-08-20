from django.dispatch.dispatcher import receiver

from calendar_mchp.signals import calendar_event_created
from user_profile.signals import enrolled
from dashboard.models import DashEvent
from dashboard.utils import DASH_EVENTS

@receiver(calendar_event_created)
def add_event(sender, **kwargs):
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

@receiver(enrolled)
def add_class_join(sender, **kwargs):
    enroll = kwargs['enroll']

    # first, send the fact that they joined to everyone already enrolled
    followers = enroll.course.student_set.all()
    print(followers)
    data = {
        'type': DASH_EVENTS.index('other class join'),
        'course': enroll.course,
        'student': enroll.student,
    }
    dash_item = DashEvent(**data)
    dash_item.save()
    for student in followers:
        dash_item.followers.add(student)
    # now give them their own dash item
    data = {
        'type': DASH_EVENTS.index('class join'),
        'course': enroll.course,
        'student': enroll.student,
    }
    dash_item = DashEvent(**data)
    dash_item.save()
    # only the student who just enrolled is intrested in knowing they just enrolled themselves
    dash_item.followers.add(enroll.student)
