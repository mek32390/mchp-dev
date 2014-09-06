from django.conf.urls import patterns, url

from notification import views

urlpatterns = patterns('',
    url(r'^mark-all/', views.mark_all_notifications, name='mark_all_notifications'),
)
