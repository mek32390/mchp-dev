from django.conf.urls import patterns, url

from calendar_mchp import views

urlpatterns = patterns('',
    url(r'^create/', views.calendar_create, name='calendar_create'),
    url(r'^update/', views.calendar_update, name='calendar_update'),
    url(r'^delete/', views.calendar_delete, name='calendar_delete'),
    url(r'^unsubscribe/', views.calendar_unsubscribe, name='calendar_unsubscribe'),

    url(r'^events/add/', views.event_add, name='event_add'),
    url(r'^events/update/', views.event_update, name='event_update'),
    url(r'^events/delete/', views.event_delete, name='event_delete'),
    url(r'^events/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),

    url(r'^preview/(?P<pk>[^/]+)', views.calendar_preview, name='calendar_preview'),

    url(r'^feed/$', views.calendar_feed, name='calendar_feed'),

    url(r'^list/$', views.calendar_list, name='calendar_list'),
                       
    url(r'^$', views.calendar, name='calendar'),
)
