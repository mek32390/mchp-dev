from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^click/(?P<uuid>[0-9a-fA-F]+)', views.clicked, name='studyguide-click'),  # noqa
    url(r'^open/(?P<uuid>[0-9a-fA-F]+)', views.opened, name='studyguide-open'),  # noqa
    url(r'^resubscribe/(?P<uuid>[0-9a-fA-F]+)', views.resubscribed, name='studyguide-resubscribe'),  # noqa
    url(r'^unsubscribe/(?P<uuid>[0-9a-fA-F]+)', views.unsubscribed, name='studyguide-unsubscribe'),  # noqa
)
