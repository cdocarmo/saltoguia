from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from .views import CrearUsuarioView, ModificarView


urlpatterns = [
    url(r'^crear/$', CrearUsuarioView.as_view(), name='crear-usuario'),
    url(r'^actualizar/$', ModificarView.as_view(), name='actualizar-usuario'),
    # url(r'^eliminar/$', 'saltoguia.views.home', name='eliminar-usuario'),
    url(r'^creado/$', TemplateView.as_view(template_name='usuarios/usuario-creado.html'), name='usuario-creado'),
]