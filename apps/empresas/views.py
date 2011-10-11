from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404,\
                        HttpResponseGone
from django.core.urlresolvers import reverse
from django.template import RequestContext
from empresas.models import Empresa
from empresas.forms import *

from django.contrib import messages
from django.utils.translation import ugettext as _

#@login_required
def crear_empresa(request, step=1):
    step = request.POST.get('step','1')
    form_Empresa = EmpresaForm()
    
    if request.method == "POST":
        
        if step == '1':
            form_Empresa = EmpresaForm(request.POST)
            
            if form_Empresa.is_valid():
                #return HttpResponse(str(step))
                empresa = form_Empresa.save(commit=False)
                empresa.save()

                form = Empresa_ServicioForm()
                return render_to_response('empresas/ingreso-de-empresa-servicio.html', 
                                          locals(), 
                                          context_instance=RequestContext(request))
        elif step == '2':
            

            form = Empresa_ServicioForm(request.POST)
            if form.is_valid():
                pass
                """
                boat_model = BoatModel(user=request.user,
                                       last_editor=request.user,
                                       name=form.cleaned_data['name'],
                                       description = form.cleaned_data['description'],
                                       length = form.cleaned_data['length'],
                                       draft = form.cleaned_data['draft'],
                                       beam = form.cleaned_data['beam'],
                                       type = form.cleaned_data['type'],
                                       designer = designer, builder = builder,
                                       hull_material = form.cleaned_data['hull_material'],
                                       hull_color = form.cleaned_data['hull_color'],
                                       year_built = form.cleaned_data['year_built'])
                boat_model.save()
                """
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