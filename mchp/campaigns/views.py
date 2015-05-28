from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import CampaignSubscriber
from .utils import (handle_click, handle_open,
                    handle_unsubscribe, handle_resubscribe)


def clicked(request, uuid):
    """ Subscriber clicked through from an e-mail.

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    handle_click(subscriber)
    url = request.GET.get('next', 'landing_page')
    return redirect(url)


def opened(request, uuid):
    """ Subscriber opened an e-mail.

    Notes
    -----
    Response code is 204 "no content," per <http://stackoverflow.com/questions/6638504/why-serve-1x1-pixel-gif-web-bugs-data-at-all>.  # noqa

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    handle_open(subscriber)
    response = HttpResponse()
    response.status_code = 204
    return response


def unsubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    Notes
    -----
    This doesn't do anything besides mark the subscriber as unsubscribed.
    A landing page and feature-specific, state-changing machinery should
    be invoked through the `next` query parameter.

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    handle_unsubscribe(subscriber)
    url = request.GET.get('next', 'landing_page')
    return redirect(url)


def resubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    Notes
    -----
    This doesn't do anything besides unmark the subscriber as unsubscribed.
    A landing page and feature-specific, state-changing machinery should
    be invoked through the `next` query parameter.

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    handle_resubscribe(subscriber)
    url = request.GET.get('next', 'landing_page')
    return redirect(url)
