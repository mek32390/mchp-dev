from django.conf import settings
from django.contrib.sites.models import Site
# from django.contrib.sites.shortcuts import get_current_site


# def current_site(request):
#     return {'current_site': get_current_site(request)}


def default_site(request):
    return {'default_site': Site.objects.get(settings.SITE_ID)}
