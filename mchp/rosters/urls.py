from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',  # noqa
<<<<<<< HEAD
    url(r'^add/$', views.RosterCreate.as_view(), name='roster-upload'),
=======
    url(r'^add/$', views.RosterSubmitView.as_view(), name='roster-upload'),

    url(r'^review/(?P<pk>\d+)/$',
        views.RosterReviewView.as_view(),
        name='roster-review'),
>>>>>>> fb3334ddd3a28741912fc30e5ab45a59d56c00cd
)
