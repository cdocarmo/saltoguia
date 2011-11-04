# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from searchs.search import SearchForm
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404,\
                        HttpResponseGone
                        
from empresas.models import Empresa, EmpresaServicio

                        
def search(request):
    search_form = SearchForm(request.GET)
    #return HttpResponse(str(search_form.search_word))
    servicios = EmpresaServicio.objects.all()
    #servicios = servicios.filter(tags__icontains=search_form.cleaned_data['search_word'])
                
    context = {
        'form': search_form,
        'servicios': servicios,
    }
    return render_to_response('search.html', context, context_instance=RequestContext(request),)