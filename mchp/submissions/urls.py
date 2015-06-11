from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns('',  # noqa
    # url(r'^dashboard/', views.CourseDashboardView.as_view(),
    #     name='course_dashboard'),
    url(r'^roster/', views.CourseSetUploadView.as_view(),
        name='course-set-upload'),
    url(r'^roster/thanks/', RedirectView().as_view(permanent=False,
            pattern_name='course-set-upload'),
        name='course-set-upload-success'),
)
