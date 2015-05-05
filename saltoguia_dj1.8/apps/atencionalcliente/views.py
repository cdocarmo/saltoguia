from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ContactoForm

# Create your views here.
class MensajeContactoView(CreateView):
    form_class = ContactoForm
    template_name = 'atencionalcliente/contacto.html'
    success_url = '/'