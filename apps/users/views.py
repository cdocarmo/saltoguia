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

            email = EmailMessage('Asunto','Probando confirmación email', 
                                 to = ['cdocarmo@cdsoft.com.uy'])
            email.send()            
            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()
    return render_to_response("registro/registro.html", {
        'form': form,
    })
