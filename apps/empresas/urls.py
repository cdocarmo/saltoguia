from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    #url(r'^$', 'empresas.views.empresa', name='empresa'),
    url(r'^nueva_empresa/$', 'empresas.views.crear_empresa', name='crear-empresa'),
    url(r'^$', 'empresas.views.ver_empresa', name='ver-empresa'),    
    url(r'^(?P<empresa_slug>[\w-]+)/(?P<servicio_slug>[\w-]+)/$', \
        'empresas.views.empresa_servicio_detalle', name='empresa-servicio-detalle'),
    
)
