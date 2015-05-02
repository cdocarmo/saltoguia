from django.conf.urls import include, url
from django.contrib import admin
from .views import IndexView, ResultadosView, \
                    DetallePublicadorView, DetalleServicioView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^resultados/$', ResultadosView.as_view(), name='resultados'),
    url(r'^detalle/publicador/(?P<publicador_id>\d+)$', DetallePublicadorView.as_view(), name='detalle-publicador'),
    url(r'^detalle/servicio/(?P<servicio_id>\d+)$', DetalleServicioView.as_view(), name='detalle-servicio'),
]