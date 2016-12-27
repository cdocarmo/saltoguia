from django.conf.urls import include, url
from .views import LoginView, LogoutView, ErrorAccesoView, AccederView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^acceder/$', AccederView.as_view(), name='acceder'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^sin-acceso/$', ErrorAccesoView.as_view(), name='sin-acceso'),
]