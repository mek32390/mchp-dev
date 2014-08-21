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
    url(r'^toggle-flag/', views.toggle_flag, name='toggle_flag'),
    url(r'^notifications/', views.notifications, name='notifications'),
    url(r'^edit-blurb/', views.edit_blurb, name='edit_blurb'),
    url(r'^edit-major/', views.edit_major, name='edit_major'),
    url(r'^edit-pic/', views.edit_pic, name='edit_pic'),
    url(r'^$', views.profile, name='my_profile'),
)
