from django.conf import settings #GF
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^_admin/', include(admin.site.urls)),
    (r'^empresas/', include('empresas.urls')),
)
#GF
if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), 
            'django.views.static.serve',
            {'document_root' : settings.MEDIA_ROOT }),)

