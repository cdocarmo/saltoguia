from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from apps.usuarios.models import Servicio


class IndexView(TemplateView):
    template_name = "buscador/index.html"


class ResultadosView(ListView):
    template_name = 'buscador/resultados.html'
    
    def get_context_data(self, **kwargs):
        context = super(ResultadosView, self).get_context_data(**kwargs)
        context['resultados'] = self.get_queryset()
        return context

    def get_queryset(self):  # temporal
        #self.publisher = get_object_or_404(Publisher, name=self.args[0])
        #return Book.objects.filter(publisher=self.publisher)
        return None


class DetallePublicadorView(TemplateView):
    # Cuando se implemente debe ser cambiada la superclase a DetailView
    template_name = "buscador/detalle.html"
    
    
class DetalleServicioView(TemplateView):
    # Cuando se implemente debe ser cambiada la superclase a DetailView
    template_name = "buscador/detalle.html"
    