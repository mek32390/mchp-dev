from django.conf.urls import patterns, url

from user_profile import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
