# coding=UTF-8
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, ugettext as u_
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import auth
from models import *
from datetime import date, datetime, timedelta
from users.forms import *
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list_detail import object_list
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage


def login(request):
    error=''
    if request.user.is_authenticated():
        HttpResponseRedirect('/')    
    login_form = LoginForm(auto_id=True)
    
    if request.method == 'POST':        
        login_form = LoginForm(request.POST, auto_id=True)
        if login_form.is_valid():
            username = request.POST['usuario']
            password = request.POST['password']
            usuario = auth.authenticate(username=username, password=password)            
            if usuario is not None and usuario.is_active:
                auth.login(request, usuario)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("Your username and password didn't match.")
            

    context = {
        'form': LoginForm,
    }
    return render_to_response(
        "login.html",
        context,
        context_instance=RequestContext(request),
    )

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            """
            email = EmailMessage('Asunto','Probando confirmación email', 
                                 to = ['cdocarmo@cdsoft.com.uy'])
            email.send()            
            """
            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()
    return render_to_response("registro/registro.html", {
        'form': form,}, context_instance=RequestContext(request),)


@login_required
def completar_perfil(request, step=1):
    step = request.POST.get('step','1')
    if step == '1': 
        try:
            empresa = Empresa.objects.get(user=request.user)
        except ObjectDoesNotExist:        
            empresa = None    
        if empresa:
            return HttpResponseRedirect(reverse('ver-empresa'))
    form_Empresa = EmpresaForm()
    #return HttpResponse(str(step))
    if request.method == "POST":
        if step == '1':
            form_Empresa = EmpresaForm(request.POST, request.FILES)
            if form_Empresa.is_valid():
                empresa = form_Empresa.save(commit=False)
                empresa.user = request.user
             
                empresa.save()
                form = Empresa_ServicioForm(initial={'empresa_id': empresa.id})
                return render_to_response('empresa/ingreso-de-empresa-servicio.html', 
                                          locals(), 
                                          context_instance=RequestContext(request)) #???
        elif step == '2':
            form_Empresa_ServicioForm = Empresa_ServicioForm(request.POST)            
            if form_Empresa_ServicioForm.is_valid():
                empresa_servicio = form_Empresa_ServicioForm.save(commit=False)
                empresa_servicio.user = request.user
                empresa_servicio.empresa = form_Empresa_ServicioForm.cleaned_data['empresa_id']
                empresa_servicio.save()
                return HttpResponseRedirect(reverse('ver-perfil'))
            
                return render_to_response('users/ver_perfil.html', 
                                          locals(), 
                                          context_instance=RequestContext(request))
    context = {
        'form': form_Empresa,
    }
    return render_to_response(
        "users/completar-perfil.html",
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
def modificar_perfil(request, slug):
    empresa = get_object_or_404(Empresa, slug = slug)
    
    if request.user.is_authenticated() and request.method == "POST":
            form = EmpresaForm(request.POST, request.FILES, instance=empresa)
            if form.is_valid():
                empresa = form.save()
                if 'nombre' in form.changed_data:
                    empresa.slug = slugify(empresa.nombre, empresa, 'slug',
                                          max_size=50)
                    empresa.save()
                return HttpResponseRedirect(empresa.get_absolute_url())
    else:
        form = EmpresaForm(instance=empresa)                
    context = {
        'form': form,
    }
    return render_to_response(
        "users/modificar_perfil.html",
        context,
        context_instance=RequestContext(request),
    )

def ver_perfil(request, empresa_slug):
    try:        
        empresa = get_object_or_404(Empresa, slug = empresa_slug)
        if request.user == empresa.user:
            servicios = EmpresaServicio.objects.filter(empresa=empresa)
        else:
            servicios = EmpresaServicio.objects.filter(empresa=empresa, status=EmpresaServicio.ACTIVA)
        return render_to_response('users/ver_perfil.html', locals(), 
                                  context_instance=RequestContext(request))
    except ObjectDoesNotExist:        
        raise Http404
