from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import CampaignSubscriber
from .utils import unsubscribe_student


def unsubscribed(request, uuid):
    """ Subscriber unsubscribed from an e-mail.

    """
    subscriber = get_object_or_404(CampaignSubscriber, uuid=uuid)
    unsubscribe_student(subscriber)
    # [TODO] proper unsubscribe page
    return HttpResponse('You have been unsubscribed successfully.')
