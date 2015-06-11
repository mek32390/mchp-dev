from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',  # noqa
    url(r'^add/$', views.RosterCreate.as_view(), name='roster-upload'),
)
