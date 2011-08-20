from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'empresas.views.crear_empresa', name='empresas'),
    
)
