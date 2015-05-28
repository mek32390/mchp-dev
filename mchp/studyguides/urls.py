from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^unsubscribe/(?P<uuid>[0-9a-fA-F]+)', views.unsubscribed, name='studyguide-unsubscribe'),  # noqa
    url(r'^resubscribe/(?P<uuid>[0-9a-fA-F]+)', views.resubscribed, name='studyguide-resubscribe'),  # noqa
)
