from django.shortcuts import get_object_or_404, redirect, render_to_response
from .models import StudyGuideCampaignSubscriber
from campaigns.utils import beacon_response


def clicked(request, uuid):
    """ Subscriber clicked through from an e-mail.

    """
    subscriber = get_object_or_404(StudyGuideCampaignSubscriber, uuid=uuid)
    subscriber.mark_clicked()
    url = request.GET.get('next', 'landing_page')
    return redirect(url)


def opened(request, uuid):
    """ Subscriber opened an e-mail.

    Notes
    -----
    Response code is 204 "no content," per <http://stackoverflow.com/questions/6638504/why-serve-1x1-pixel-gif-web-bugs-data-at-all>.  # noqa

    """
    subscriber = get_object_or_404(StudyGuideCampaignSubscriber, uuid=uuid)
    subscriber.mark_opened()
    return beacon_response(subscriber)


def unsubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    """
    subscriber = get_object_or_404(StudyGuideCampaignSubscriber, uuid=uuid)
    subscriber.mark_unsubscribed()
    return render_to_response('studyguides/unsubscribed_page.html', {
        'subscriber': subscriber,
        'course': subscriber.campaign.event.calendar.course})


def resubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    """
    subscriber = get_object_or_404(StudyGuideCampaignSubscriber, uuid=uuid)
    subscriber.mark_resubscribed()
    return render_to_response('studyguides/resubscribed_page.html', {
        'subscriber': subscriber,
        'course': subscriber.campaign.event.calendar.course})
