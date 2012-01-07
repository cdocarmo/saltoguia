# coding=UTF-8

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'searchs.views.index', name='buscar'),
    url(r'^servicios/$', 'searchs.views.result_search', name = 'demo-search'),
    url(r'^get_tags/$', 'searchs.views.cargo_tags_json', name="cargo-tags-json"),    
)
