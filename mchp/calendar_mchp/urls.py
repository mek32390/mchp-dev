from django.conf.urls import patterns, url

from calendar_mchp import views

urlpatterns = patterns('',
    url(r'^create/', views.calendar_create, name='calendar_create'),
    url(r'^delete/', views.calendar_delete, name='calendar_delete'),
    url(r'^events/add/', views.event_add, name='event_add'),

    url(r'^preview/(?P<uuid>[^/]+)', views.calendar_preview, name='calendar_preview'),

    url(r'^$', views.calendar, name='calendar'),
)
