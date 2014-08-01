from django.conf.urls import patterns, url

from referral import views

urlpatterns = patterns('',
    url(r'^redeem/', views.redeem, name='referral_redeem'),
)
