from django.conf.urls import include, url
from .views import MensajeContactoView


urlpatterns = [
    url(r'^crear/$', MensajeContactoView.as_view(), name='contacto'),
]