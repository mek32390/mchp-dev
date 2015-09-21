from django.utils import timezone

from collections import Counter
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
    events = CalendarEvent.objects.exclude(notify_lead=None).filter(
        start__gte=now, notify_lead__gt=0, calendar__primary=True)
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


def _rank_documents(event):
    """ Return likely primary document candidates.

    Parameters
    ----------
    event : calendar_mchp.models.CalendarEvent
        An event whose documents should be ranked.

    Returns
    -------
    out : list
        The top-ranked (tier one) event documents.

    """
    def rank(items, key, score=1):
        """ Create a Counter and rank items.

        Parameters
        ----------
        items : iterable
            Items to rank.
        key : function
            A function to run for sorting and ranking `items`.
        score : number, optional
            A multiplier for each ranking.

        Notes
        -----
        TODO: Clean up this method a bit, especially with the `counts1` var.

        """
        counter = Counter({item: 0 for item in items})
        if key:
            count_per_val = [key(item) for item in items]
            counts1 = sorted(set(count_per_val))
            counts = {n: counts1.index(n) + 1 for n in counts1}
            for item in sorted(items, key=key):
                counter[item] = score * counts[key(item)]
        return counter

    event = event
    documents = event.documents.all()

    print (documents.count())

    # get all enrollments (student and join date)
    enrollments = Enrollment.objects.filter(
        course=event.calendar.course)

    scores = rank(documents, None)

    scores += rank(documents,
                   lambda doc: doc.create_date,
                   score=40)

    scores += rank(documents,
                   lambda doc: doc.purchased_document.count(),
                   score=30)

    scores += rank(documents,
                   lambda doc: enrollments.get(
                       student=doc.owner).join_date,
                   score=20)

    scores += rank(documents,
                   lambda doc: doc.rating(),
                   score=10)

    print('DEBUG: SCORES = ' + str(scores))
    top_score = scores.most_common(1)
    if top_score:
        top_score = top_score[0][1]
        return [d for d in documents if scores[d] == top_score]
    else:
        return []
