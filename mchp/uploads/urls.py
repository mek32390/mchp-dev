from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns('',  # noqa
    # url(r'^dashboard/', views.CourseDashboardView.as_view(),
    #     name='course_dashboard'),
    url(r'^roster/', views.RosterUploadView.as_view(),
        name='roster-upload'),
    url(r'^roster/thanks/', views.RosterUploadSuccessView.as_view(),
        name='roster-upload-success'),
)
