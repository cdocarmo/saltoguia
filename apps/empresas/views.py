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
def crear_empresa(request):
    form_Empresa = EmpresaForm()
    if request.method == "POST":
        form_Empresa = EmpresaForm(request.POST)
        if form_Empresa.is_valid():
            empresa = form_Empresa.save(commit=False)
            empresa.save()
            messages.add_message(request, messages.INFO,
                                 mensaje('EmpresaCreada'))
            return HttpResponseRedirect('/empresas')

    context = {
        'form': form_Empresa,
    }
    return render_to_response(
        "empresas/crear_empresa.html",
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