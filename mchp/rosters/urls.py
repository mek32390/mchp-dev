from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',  # noqa
    url(r'^add/$', views.RosterSubmitView.as_view(), name='roster-upload'),

    url(r'^review/(?P<pk>\d+)/$',
        views.RosterReviewView.as_view(),
        name='roster-review'),

    url(r'^list/$', views.RosterListView.as_view(), name='roster-list'),
)