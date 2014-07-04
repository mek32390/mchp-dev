from django.conf.urls import patterns, url

from document import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='document_index'),
)
