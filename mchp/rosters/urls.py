from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',  # noqa
    url(r'^add/$', views.RosterCreateView.as_view(), name='roster-upload'),
    url(r'^detail/(?P<pk>\d+)/$', views.RosterDetailView.as_view(),
        name='roster-detail'),
)
