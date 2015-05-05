# -*- coding: utf-8 -*-
from django import forms
from .models import MensajeContacto


class ContactoForm(forms.ModelForm):
    nombres = forms.CharField(label=u'Nombres')
    apellidos = forms.CharField(label=u'Apellidos')
    email = forms.CharField(label=u'Email')
    comentarios = forms.CharField(label=u'Comentarios', widget=forms.Textarea)
    
    class Meta:
        model = MensajeContacto
        fields = ('nombres', 'apellidos', 'email', 'comentarios',)
