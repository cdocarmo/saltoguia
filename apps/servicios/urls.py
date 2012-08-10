from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    #url(r'^$', 'empresas.views.empresa', name='empresa'),
    url(r'^nueva_empresa/$', 'empresa.views.crear_empresa', name='crear-empresa'),
    url(r'^([-\w]+)/modificar/$', 'empresa.views.modificar_empresa', name="modificar-empresa"),
    url(r'^([-\w]+)/([-\w]+)/modificar/$', 'empresa.views.modificar_servicio', name="modificar-servicio"),
    url(r'^(?P<empresa_slug>[\w-]+)/nuevo_servicio/$', 'empresa.views.nuevo_servicio', name='nuevo-servicio'),
    url(r'^(?P<empresa_slug>[\w-]+)/$', 'empresa.views.empresa', name='empresa'),
    url(r'^$', 'empresa.views.ver_empresa', name='ver-empresa'),    
    url(r'^(?P<empresa_slug>[\w-]+)/(?P<servicio_slug>[\w-]+)/$', \
        'empresa.views.empresa_servicio_detalle', name='empresa-servicio-detalle'),
    
)
