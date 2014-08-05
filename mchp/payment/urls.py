from django.conf.urls import patterns, url

from payment import views

urlpatterns = patterns('',
    url(r'^save-info/', views.save_info, name='save_info'),
    url(r'^charge/', views.charge, name='stripe_charge'),
)