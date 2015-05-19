from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Subscriber

def campaign_open(request, token):
    """ Subscriber opened an e-mail.

    """
    subscriber = Subscriber.objects.get_object_or_404(token=token)
    subscriber.opens += 1
    subscriber.save(updated_fields=['opens'])
    return HttpResponse()


def campaign_click(request, token):
    """ Subscriber clicked through.

    """
    subscriber = Subscriber.objects.get_object_or_404(token=token)
    subscriber.clicks += 1
    subscriber.save(updated_fields=['clicks'])
    return HttpResponse()


def campaign_unsubscribe(request, token):
    """ Subscriber unsubscribed.  :'(

    """
    subscriber = Subscriber.objects.get_object_or_404(token=token)
    subscriber.unsubscribes += 1
    subscriber.save(updated_fields=['unsubscribes'])
    return HttpResponse()
