from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^unsubscribe/(?P<uuid>[0-9a-fA-F]+)', views.unsubscribed, name='course-unsubscribe'),
)
