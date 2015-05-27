from django.shortcuts import get_object_or_404
from .models import CampaignSubscriber
from .utils import (subscriber_clicked, subscriber_opened,
                    subscriber_unsubscribed)


def clicked(request, uuid):
    """ Subscriber clicked through from an e-mail.

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    return subscriber_clicked(request, subscriber)


def opened(request, uuid):
    """ Subscriber opened an e-mail.

    Notes
    -----
    Response code is 204 "no content," per <http://stackoverflow.com/questions/6638504/why-serve-1x1-pixel-gif-web-bugs-data-at-all>.  # noqa

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    return subscriber_opened(request, subscriber)


def unsubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    return subscriber_unsubscribed(request, subscriber)
