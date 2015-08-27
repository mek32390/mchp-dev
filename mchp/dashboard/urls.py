from django.conf.urls import patterns, url

from dashboard import views

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^new_homepage/', views.new_homepage, name='new_homepage'),
    url(r'^feed/', views.feed, name='dashboard_feed'),
    url(r'^rss-proxy/', views.rss_proxy, name='dashboard_rss_proxy'),
    url(r'^toggle-rss/', views.toggle_rss, name='toggle_rss'),
)
