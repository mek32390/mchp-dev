from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from documents import views

urlpatterns = patterns('',
    url(r'^add/', views.document_upload, name='document_upload'),
    url(r'^remove/', views.document_delete, name='document_delete'),
    url(r'^unpurchase/', views.purchase_delete, name='purchase_delete'),
    url(r'^review/', views.purchase_update, name='purchase_update'),

    url(r'^$', views.document_list, name='document_list'),

    url(r'^fetch-preview/', views.fetch_preview, name='fetch_preview'),

    url(r'^preview/(?P<uuid>[^/]+)', views.document_preview, name='document_preview'),

    url(r'^(?P<uuid>[^/]+)/[^/]+/', 
        RedirectView.as_view(url=reverse_lazy('document_detail'))),
    url(r'^(?P<uuid>[^/]+)/', views.document_detail, name='document_detail'),
)
