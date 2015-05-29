from django.shortcuts import get_object_or_404, render_to_response
from .models import StudyGuideCampaignSubscriber
from .utils import unsubscribe_student, resubscribe_student


def unsubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    """
    subscriber = get_object_or_404(StudyGuideCampaignSubscriber, uuid=uuid)
    unsubscribe_student(subscriber)
    return render_to_response('studyguides/unsubscribed_page.html', {
        'subscriber': subscriber,
        'course': subscriber.campaign.event.calendar.course})


def resubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    """
    subscriber = get_object_or_404(StudyGuideCampaignSubscriber, uuid=uuid)
    resubscribe_student(subscriber)
    return render_to_response('studyguides/resubscribed_page.html', {
        'subscriber': subscriber,
        'course': subscriber.campaign.event.calendar.course})
