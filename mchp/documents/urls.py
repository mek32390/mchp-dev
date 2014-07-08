from django.conf.urls import patterns, url

from document import views

urlpatterns = patterns('',
    # url(r'^add/', views.index, name='document_index'),
    #                    # fix these two
    # url(r'^view/[1-9]', views.index, name='document_index'),
    # url(r'^[1-9]', views.index, name='document_index'),

    url(r'^$', views.index, name='document_index'),
)
