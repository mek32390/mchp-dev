from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^open/(?P<uuid>[0-9a-fA-F]+)', views.opened, name='course-open'),  # noqa
    url(r'^click/(?P<uuid>[0-9a-fA-F]+)', views.clicked, name='course-click'),  # noqa
    url(r'^unsubscribe/(?P<uuid>[0-9a-fA-F]+)', views.unsubscribed, name='course-unsubscribe'),  # noqa
)
