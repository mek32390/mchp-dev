from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from .models import CampaignSubscriber


def clicked(request, uuid):
    """ Subscriber clicked through from an e-mail.

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    subscriber.clicked = timezone.now()
    subscriber.save(update_fields=['clicked'])
    url = request.GET.get('next', 'landing_page')
    return redirect(url)


def opened(request, uuid):
    """ Subscriber opened an e-mail.

    Notes
    -----
    Response code is 204 "no content," per <http://stackoverflow.com/questions/6638504/why-serve-1x1-pixel-gif-web-bugs-data-at-all>.  # noqa

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    subscriber.opened = timezone.now()
    subscriber.save(update_fields=['opened'])
    response = HttpResponse()
    response.status_code = 204
    return response


def unsubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    subscriber.unsubscribed = timezone.now()
    subscriber.save(update_fields=['unsubscribed'])
    url = request.GET.get('next', 'landing_page')
    return redirect(url)
