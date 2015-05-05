from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.utils.html import strip_tags

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

def make_email_message(subject, body, sender, recipient, connection):
    """ Build an EmailMessage with HTML and plain text alternatives.

    Parameters
    ----------
    subject : str
        A subject for this message.  Limited to 78 characters.
    body : str
        A body for this message.
    sender : str
        An e-mail address (and optional name) from which to send this message.
    recipient : str
        An e-mail address to which to deliver this message.
    connection : django.core.mail.backends.console.EmailBackend
        A connection through which to send the message.

    """
    msg = EmailMultiAlternatives(subject, strip_tags(body),
                                 sender, [recipient],
                                 connection=connection)
    msg.attach_alternative(body, "text/html")
    return msg

