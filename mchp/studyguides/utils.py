from django.utils import timezone

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
