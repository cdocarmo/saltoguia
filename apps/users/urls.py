from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'users.views.login', name='login'),
    url(r'^registro/$', 'users.views.register', name='registro'),
    url(r'^logout/$', 'users.views.logout', name='logout'),
    url(r'^completar_perfil/$', 'users.views.completar_perfil', name='completar-perfil'),
    url(r'^([-\w]+)/modificar/$', 'users.views.modificar_perfil', name="modificar-perfil"),
    url(r'^$', 'users.views.ver_perfil', name='ver-perfil'),
)
