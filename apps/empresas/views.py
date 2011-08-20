from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404,\
                        HttpResponseGone
from django.core.urlresolvers import reverse
from django.template import RequestContext
from empresas.models import Empresa
from empresas.forms import *


#@login_required
def crear_empresa(request):
    form_Empresa = EmpresaForm()
    if request.method == "POST":
        form_Empresa = EmpresaForm(request.POST)
        if form_Empresa.is_valid():
            empresa = form_Empresa.save(commit=False)
            empresa.save()

            #return HttpResponseRedirect('/entities')

    context = {
        'form': form_Empresa,
    }
    return render_to_response(
        "empresas/crear_empresa.html",
        context,
        context_instance=RequestContext(request),
    )

