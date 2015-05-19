from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^open/(?P<uuid>[0-9a-fA-F]+)', views.campaign_open, name='campaign-open'),
    url(r'^click/(?P<uuid>[0-9a-fA-F]+)', views.campaign_click, name='campaign-click'),
    url(r'^unsubscribe/(?P<uuid>[0-9a-fA-F]+)', views.campaign_unsubscribe, name='campaign-unsubscribe'),
)
