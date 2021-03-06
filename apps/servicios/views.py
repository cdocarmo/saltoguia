from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404,\
                        HttpResponseGone
from django.core.urlresolvers import reverse
from django.template import RequestContext
from servicios.models import Servicio
from servicios.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist
from utilita.util import unique_slugify




@login_required
def ver_empresa(request):
    try:        
        empresa = Empresa.objects.get(user=request.user)
        servicios = EmpresaServicio.objects.filter(empresa=empresa)
        return render_to_response('empresa/ver_empresa.html', locals(), 
                                  context_instance=RequestContext(request))
    except ObjectDoesNotExist:        
        return HttpResponseRedirect(reverse('crear-empresa'))
        

def empresa_servicio_detalle(request, empresa_slug, servicio_slug):
       
    empresa = get_object_or_404(Empresa, slug = empresa_slug)
    servicio = EmpresaServicio.objects.get(empresa=empresa, slug = servicio_slug)

    return render_to_response('empresa/ver_servicio.html', locals(), 
                              context_instance=RequestContext(request))
    

@login_required
def nuevo_servicio(request):
    # le quite el argumento empresa_slug
    # TODO: Aqui hay que cambiar todos el algoritmo
    # que antes llamaba a Empresa
    try:
        usuario = Empresa.objects.get(slug = empresa_slug, user = request.user)
    except ObjectDoesNotExist:        
        return HttpResponseRedirect(reverse('crear-empresa'))
    form = Empresa_ServicioForm(initial={'empresa_id': empresa.id})    
    if request.method == "POST":
        form_Empresa_ServicioForm = Empresa_ServicioForm(request.POST)        
        if form_Empresa_ServicioForm.is_valid():    
            empresa_servicio = form_Empresa_ServicioForm.save(commit=False)
            empresa_servicio.user = request.user
            empresa_servicio.empresa = empresa #form_Empresa_ServicioForm.cleaned_data['empresa_id']
            empresa_servicio.save()                
    
            return HttpResponseRedirect(reverse('ver-empresa'))            
    return render_to_response('empresa/ingreso-de-empresa-servicio.html', 
                              locals(), 
                              context_instance=RequestContext(request))                   


@login_required
def modificar_servicio(request, slug_Empresa, slug_Servicio):
    empresa = get_object_or_404(Empresa, slug = slug_Empresa)
    servicio = EmpresaServicio.objects.get(empresa=empresa, slug=slug_Servicio) 
    if request.user.is_authenticated() and request.method == "POST":
        form = Modificar_ServicioForm(request.POST)       
        #return HttpResponse(str(form))
        if form.is_valid():
            post = request.POST.copy()
            servicio.descripcion = post['descripcion']
            servicio.nombre =  post['nombre']
            servicio.tags = post['tags']
            servicio.save()
            return HttpResponseRedirect(empresa.get_absolute_url())
    else:
        form = Modificar_ServicioForm()
    context = {
        'form': form,
    }    
    return render_to_response(
        "empresa/modificar-servicio.html", {'servicio_form': form,
                                            'nombre': servicio.nombre, 'descripcion': servicio.descripcion,
                                            'tags': servicio.tags, 'empresa': empresa},
        context_instance=RequestContext(request),
    )

