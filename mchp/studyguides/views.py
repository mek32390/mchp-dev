from django.shortcuts import get_object_or_404, render_to_response
from campaigns.models import CampaignSubscriber
from .models import StudyGuideAnnouncement
from .utils import unsubscribe_student, resubscribe_student


def unsubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    unsubscribe_student(subscriber)

    announcement = StudyGuideAnnouncement.objects.get(
        campaign=subscriber.campaign)
    return render_to_response('studyguides/unsubscribed_page.html', {
        'subscriber': subscriber,
        'course': announcement.event.calendar.course})


def resubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    resubscribe_student(subscriber)
    announcement = StudyGuideAnnouncement.objects.get(
        campaign=subscriber.campaign)
    return render_to_response('studyguides/resubscribed_page.html', {
        'subscriber': subscriber,
        'course': announcement.event.calendar.course})
