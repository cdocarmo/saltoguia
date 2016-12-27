from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.contrib.auth.models import User


class LoginView(TemplateView):
    template_name = 'acceso/login.html'
    
        
class AccederView(View):
    def post(self, request):
        # print request.POST
        try:
            usuario = User.objects.get(email__exact=request.POST.get('email'))
        except:
            return HttpResponseRedirect('/acceso/sin-acceso/')
        
        # print usuario.username
        password = request.POST.get('password')
        usuario = auth.authenticate(username=usuario.username, password=password)
        # print usuario
        if usuario is not None and usuario.is_active:
            auth.login(request, usuario)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/acceso/sin-acceso/')
        
    
class LogoutView(TemplateView):
    template_name = '/'
    
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect('/')
    
class ErrorAccesoView(TemplateView):
    template_name = 'acceso/error-login.html'