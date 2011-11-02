from django.contrib.admin import site, ModelAdmin, TabularInline, StackedInline
from empresas.models import Empresa, EmpresaServicio


class EmpresaAdmin(ModelAdmin):
    list_display = ('nombre', 'domicilio', 'telefono', 'celular', 'mail', 'descripcion')
    search_fields = ('nombre', 'mail')
    
class EmpresaServicioAdmin(ModelAdmin):
    list_display = ('nombre', 'empresa', 'descripcion', 'status', 'tags', 'tipo')
    search_fields = ('nombre', 'tags')
        
site.register(Empresa, EmpresaAdmin)
site.register(EmpresaServicio, EmpresaServicioAdmin)

    