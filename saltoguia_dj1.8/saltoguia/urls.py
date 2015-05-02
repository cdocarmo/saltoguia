from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect
from apps.usuarios import urls as usuarios_urls
from apps.buscador import urls as buscador_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'saltoguia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(buscador_urls)),
    url(r'^usuarios/', include(usuarios_urls)),
    url(r'^admin/', include(admin.site.urls)),
]


handler404=lambda request: redirect(to='/', permanent=True)