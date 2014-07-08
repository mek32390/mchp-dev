from django.conf.urls import patterns, url

from user_profile import views

urlpatterns = patterns('',
    url(r'^confirm-school/', views.confirm_school, name='confirm_school'),
    url(r'^get-email/', views.get_email, name='get_email'),
    url(r'^resend-email/', views.resend_email, name='resend_email'),
                       #redirect this later
    url(r'^documents/', views.resend_email, name='resend_email'),
    url(r'^$', views.profile, name='user_profile'),
)
