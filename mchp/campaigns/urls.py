from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^open/(?P<uuid>[0-9a-fA-F]+)', views.opened, name='campaign-open'),
    url(r'^click/(?P<uuid>[0-9a-fA-F]+)', views.clicked, name='campaign-click'),
    url(r'^unsubscribe/(?P<uuid>[0-9a-fA-F]+)', views.unsubscribed, name='campaign-unsubscribe'),
)
