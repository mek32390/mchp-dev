from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.utils.html import strip_tags

from datetime import timedelta
# from . import models
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


# def campaign_for_event(event):
#     """ Create a campaign for an event.

#     Parameters
#     ----------
#     event : calendar_mchp.models.CalendarEvent
#         An event to check.

#     Returns
#     -------
#     out : campaigns.models.Campaign
#         An e-mail campaign.

#     """
#     lead = timedelta(minutes=event.notify_lead)
#     template = None
#     campaign = models.Campaign.objects.create(template=template,
#                                               when=event.start - lead,
#                                               until=event.start)
#     proposed_recipients = []
#     for r in proposed_recipients:
#         campaign.subscribers.add(r)
#     campaign.save()
#     return campaign


def students_for_event(event):
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
    return [e.student for e in enrollments if e.student.user.is_active]


def make_email_message(subject, body, sender, recipient, connection):
    """ Build an EmailMessage with HTML and plain text alternatives.

    Parameters
    ----------
    subject : str
        A subject for this message.  Limited to 78 characters.
    body : str
        A body for this message.
    sender : str
        An e-mail address (and optional name) from which to send.
    recipient : str
        An e-mail address (and optional name) to which to send.
    connection : django.core.mail.backends.console.EmailBackend
        A connection through which to send the message.

    """
    msg = EmailMultiAlternatives(subject, strip_tags(body),
                                 sender, [recipient],
                                 connection=connection)
    msg.attach_alternative(body, "text/html")
    return msg
