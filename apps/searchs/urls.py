# coding=UTF-8

from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'searchs.views.search', name='buscar'),
    
)
