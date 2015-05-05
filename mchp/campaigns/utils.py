from django.utils import timezone

from datetime import timedelta
from calendar_mchp.models import CalendarEvent
from schedule.models import Enrollment

def upcoming_events():
    """ Events with notifications due.

    Returns
    -------
    out : list
        A list of events.

    """
    now = timezone.now()
    events = CalendarEvent.objects.filter(start__gte=now,
                                          notify_lead__gt=0)
    return [event for event in events
            if now > event.start - timedelta(minutes=event.notify_lead)]


def subscribers_for_event(event):
    """ Determine students associated with an event.

    Parameters
    ----------
    event : calendar_mchp.models.CalendarEvent
        An event to check.

    Returns
    -------
    out : list
        A list of dicts of students who want to receive e-mail.

    """
    enrollments = Enrollment.objects.filter(course=event.calendar.course,
                                            receive_email=True)
    return [enrollment.student for enrollment in enrollments
            if enrollment.student.user.is_active]


def upcoming_event_subscribers():
    """ Deduplicated collection of subscribers.

    Returns
    -------
    out : tuple of user_profile.models.Student
        A tuple of students to be notified.

    """
    subscribers = []
    for event in upcoming_events():
        subscribers.extend(subscribers_for_event(event))
    return tuple(set(subscribers))

def notinuse_test():
    "Create campaign for event"
    # Campaign()
