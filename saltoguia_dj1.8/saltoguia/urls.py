from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from apps.usuarios import urls as usuarios_urls
from apps.buscador import urls as buscador_urls
from apps.atencionalcliente import urls as atencioncli_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'saltoguia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(buscador_urls)),
    url(r'^usuarios/', include(usuarios_urls)),
    url(r'^atencion-al-cliente/', include(atencioncli_urls)),
    url(r'^desarrollo/$', TemplateView.as_view(template_name='estaticas/desarrollo.html'), name='desarrollo'),
    url(r'^acerca-de/$', TemplateView.as_view(template_name='estaticas/acerca-de.html'), name='acerca-de'),
    url(r'^condiciones-de-uso/$', TemplateView.as_view(template_name='estaticas/condiciones-de-uso.html'), name='condiciones'),
    url(r'^admin/', include(admin.site.urls)),
]


handler404=lambda request: redirect(to='/', permanent=True)