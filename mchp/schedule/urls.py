from django.conf.urls import patterns, url

from schedule import views

urlpatterns = patterns('',
    url(r'^course/create/', views.course_create, name='course_create'),
    url(r'^course/remove/', views.course_remove, name='course_remove'),
    url(r'^course/add/', views.course_add, name='course_add'),
    url(r'^course/(?P<number>\d+)/(?P<slug>[^/]+)/$', views.course, name='course_slug'),
    url(r'^course/(?P<number>\d+)/$', views.course, name='course'),
    url(r'^(?P<number>\d+)/', views.school, name='school'),
)
