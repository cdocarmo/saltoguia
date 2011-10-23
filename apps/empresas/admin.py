from django.contrib.admin import site, ModelAdmin, TabularInline, StackedInline
from empresas.models import Empresa


class EmpresaAdmin(ModelAdmin):
    list_display = ('nombre', 'domicilio', 'telefono', 'celular', 'mail', 'descripcion')
    search_fields = ('nombre', 'mail')
    
site.register(Empresa, EmpresaAdmin)


