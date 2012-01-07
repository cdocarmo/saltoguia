# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import simplejson

from empresa.models import Empresa, EmpresaServicio

def search(request):
    search_form = SearchForm(request.GET)
    servicios = EmpresaServicio.objects.filter(status=EmpresaServicio.ACTIVA)
    if search_form.is_valid():    
        servicios = servicios.filter(tags__icontains=search_form.cleaned_data['search'])                
    context = {
        'form': search_form,
        'servicios': servicios,
    }
    return render_to_response('search.html', context, context_instance=RequestContext(request),)



def index( request ):    
    template = 'search.html'
    data = {}
    return render_to_response( template, data, 
                               context_instance = RequestContext( request ), )

def result_search( request ):
    servicios = EmpresaServicio.objects.filter(status=EmpresaServicio.ACTIVA)
    if request.is_ajax():
        q = request.GET.get( 'q' )
        if q is not None:  
            results = servicios.filter(
                                       Q( empresa__nombre__icontains = q ) |
                                       Q( nombre__icontains = q ) |
                                       Q( tags__icontains = q ) ).order_by( 'nombre' )

            template = 'resultado.html'
            data = {
                'results': results,
            }
            return render_to_response( template, data, 
                                       context_instance = RequestContext( request ) )
            
            
def cargo_tags_json(request):
    servicios = EmpresaServicio.objects.filter(status=EmpresaServicio.ACTIVA).values('id', 'nombre')

    response=HttpResponse(mimetype="application/javascript")
    response.write(simplejson.dumps(list(servicios)))

    return response            