from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404,\
                        HttpResponseGone
from django.core.urlresolvers import reverse
from django.template import RequestContext
from empresas.models import Empresa, EmpresaServicio
from empresas.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist

@login_required
def crear_empresa(request, step=1):
    step = request.POST.get('step','1')
    form_Empresa = EmpresaForm()
    #return HttpResponse(str(step))
    if request.method == "POST":
        
        if step == '1':
            form_Empresa = EmpresaForm(request.POST)
            
            if form_Empresa.is_valid():
                #return HttpResponse(str(step))
                empresa = form_Empresa.save(commit=False)
                empresa.user = request.user
                empresa.save()

               
                form = Empresa_ServicioForm(initial={'empresa_id': empresa.id})
                return render_to_response('empresas/ingreso-de-empresa-servicio.html', 
                                          locals(), 
                                          context_instance=RequestContext(request))
        elif step == '2':

            form_Empresa_ServicioForm = Empresa_ServicioForm(request.POST)
            
            if form_Empresa_ServicioForm.is_valid():

                empresa_servicio = form_Empresa_ServicioForm.save(commit=False)
                empresa_servicio.user = request.user
                empresa_servicio.empresa = form_Empresa_ServicioForm.cleaned_data['empresa_id']
                empresa_servicio.save()                

                return render_to_response('empresas/ingreso-de-empresa-servicio.html', 
                                          locals(), 
                                          context_instance=RequestContext(request))
    context = {
        'form': form_Empresa,
    }
    return render_to_response(
        "empresas/ingreso-de-empresa.html",
        context,
        context_instance=RequestContext(request),
    )



def mensaje(action, url=False):
    try:
        result = _({
            'EmpresaCreada': "La Empresa fue creada \
                              .",
        }.get(action))

    except KeyError:
        result = _('Sin Mensaje')

    return result


@login_required
def ver_empresa(request):
    try:        
        empresa = Empresa.objects.get(user=request.user)
        servicios = EmpresaServicio.objects.filter(empresa=empresa) 
        return render_to_response('empresas/ver_empresa.html', locals(), context_instance=RequestContext(request))
    except ObjectDoesNotExist:        
        return HttpResponseRedirect(reverse('crear-empresa'))
        
        
def empresa_servicio_detalle(request, empresa_slug, servicio_slug):
    pass
    """
    boat_model = get_object_or_404(BoatModel, slug = slug)

    administrator = boat_model.administered_by(request.user)

    content_type = ContentType.objects.get_for_model(boat_model)
    pools = Pool.objects.filter(content_type__pk=content_type.id, object_id=boat_model.id).order_by('-created_at')
    pool_count = Pool.objects.filter(content_type__pk=content_type.id, object_id=boat_model.id).count()
    pool_show_all = pool_count > 6


    return render_to_response('boats/boat_model_detail.html', locals(), context_instance=RequestContext(request))
    """
