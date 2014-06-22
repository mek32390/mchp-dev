from django.conf.urls import patterns, url

from user_profile import views

urlpatterns = patterns('',
    url(r'^confirm-school/', views.confirm_school, name='confirm_school'),
    url(r'^$', views.index, name='index'),
)
