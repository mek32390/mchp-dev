from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from documents import views

urlpatterns = patterns('',
    url(r'^add/', views.document_upload, name='document_upload'),
    url(r'^$', views.document_list, name='document_list'),

    url(r'^preview/(?P<uuid>[^/]+)/[^/]+/', 
        RedirectView.as_view(url=reverse_lazy('document_preview'))),
    url(r'^preview/(?P<uuid>[^/]+)/', views.document_preview, name='document_preview'),

    url(r'^(?P<uuid>[^/]+)/[^/]+/', 
        RedirectView.as_view(url=reverse_lazy('document_detail'))),
    url(r'^(?P<uuid>[^/]+)/', views.document_detail, name='document_detail'),
)
