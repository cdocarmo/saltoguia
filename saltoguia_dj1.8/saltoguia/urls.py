from django.conf.urls import include, url
from django.contrib import admin
from apps.usuarios import urls as usuarios_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'saltoguia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^usuarios/', include(usuarios_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
