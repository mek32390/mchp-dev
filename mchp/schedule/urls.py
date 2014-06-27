from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from schedule import views

urlpatterns = patterns('',
    url(r'^course/create', views.course_create, name='course_create'),
    url(r'^course/remove', views.course_remove, name='course_remove'),
    url(r'^course/add', views.course_add, name='course_add'),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('user_profile'))),
)
