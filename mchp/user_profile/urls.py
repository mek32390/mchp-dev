from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from user_profile import views

urlpatterns = patterns('',
    url(r'^confirm-school/', views.confirm_school, name='confirm_school'),
    url(r'^get-email/', views.get_email, name='get_email'),
    url(r'^resend-email/', views.resend_email, name='resend_email'),
    url(r'^documents/', RedirectView.as_view(url=reverse_lazy('document_list'))),
    url(r'^(?P<number>\d+)/', views.profile, name='profile'),
    url(r'^$', views.profile, name='my_profile'),
)
