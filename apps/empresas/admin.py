from django.contrib.admin import site, ModelAdmin, TabularInline, StackedInline
from empresas.models import Empresa, EmpresaServicio



def activar_Servicio(modeladmin, request, queryset):
    queryset.update(status='2')
activar_Servicio.short_description = "Activar Servicios Seleccionados"

def desactivar_Servicio(modeladmin, request, queryset):
    queryset.update(status='3')
desactivar_Servicio.short_description = "Desactivar Servicios Seleccionados"

    

class EmpresaAdmin(ModelAdmin):
    list_display = ('nombre', 'domicilio', 'telefono', 'celular', 'mail', 'descripcion')
    search_fields = ('nombre', 'mail')
    
class EmpresaServicioAdmin(ModelAdmin):
    list_display = ('nombre', 'empresa', 'descripcion', 'status', 'tags', 'tipo')
    search_fields = ('nombre', 'tags')
    actions = [activar_Servicio, desactivar_Servicio]
        
site.register(Empresa, EmpresaAdmin)
site.register(EmpresaServicio, EmpresaServicioAdmin)

    