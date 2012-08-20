# coding=UTF-8
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms
# from django.contrib.auth.models import User
from models import UserProfile
from datetime import date, datetime, timedelta
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    usuario = forms.CharField(label=_(u'Usuario'), max_length=100, 
                              widget=forms.TextInput(attrs={'class':'input-text'}))
    password = forms.CharField(label=_(u'Password'), 
                               widget=forms.PasswordInput(attrs={'class':'input-text'}))

    def as_br(self):
        """
        GF
        Based in as_p, from superclass forms.py.
        Returns this form rendered as HTML <br />s.
        """
        return self._html_output(
            normal_row = u'%(label)s <br />%(field)s%(help_text)s <br />',
            error_row = u'%s',
            row_ender = '',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)


class RegisterForm(UserCreationForm):
    username = forms.CharField(label=_(u'*Usuario'), max_length=30, widget=forms.TextInput(attrs={'class':'input-text'}))
    email = forms.EmailField(label = "*Email", widget=forms.TextInput(attrs={'class':'input-text'}), 
            error_messages={'invalid': 'Escriba una dirección de e-mail válida.'})
    #override password1 and password2 from UserCreationForm
    password1 = forms.CharField(label=_("*Password"), widget=forms.PasswordInput(attrs={'class':'input-text'}))
    password2 = forms.CharField(label=_("*Password confirmation"), widget=forms.PasswordInput(attrs={'class':'input-text'}),
        help_text = _("Enter the same password as above, for verification."))
    validation = forms.BooleanField(label="*Validacion", widget=forms.CheckboxInput(), help_text = "Acepto que estos datos \
        sean almacenados en la base de datos de saltoguia.com.uy. (Estos datos pueden ser elimnados en el momento que usted desee.)")
    
    def as_br(self):
        """
        GF
        Based in as_p, from superclass forms.py.
        Returns this form rendered as HTML <br />s.
        """
        return self._html_output(
            normal_row = u'%(label)s <br />%(field)s%(help_text)s <br />',
            error_row = u'%s',
            row_ender = '',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)
    
    class Meta:
        model = User
        fields = ("username", "email", )

class CompleteProfile(forms.Form):
    
    ayudas = {
              'nombre':u'Ingresa el nombre de tu empresa o el tuyo propio si ofreces un servicio particular.',
              'domicilio':u'Ingresa una direcci\xf3n, si corresponde.',
              'telefono':u'Ingresa un n\xfamero telef\xf3nico fijo.',
              'celular':u'Ingresa el n\xfamero de tu m\xf3vil.',
              'mail':u'Ingresa una direcci\xf3n de email de tu empresa o tu servicio.',
              'descripcion':u'Escribe una breve descripci\xf3n de tu empresa o del servicio que ofreces.',
              'tipo':u'Selecciona si eres un empresa o una persona que ofrece alg\xfan servicio.',
              'documento':u'Si eres empresa coloca tu R.U.T. sino tu c\xe9dula.',
              'web':u'Si tienes un sitio web coloca la direcci\xf3n url (tambi\xe9n puede colocar la url de tu p\xe1gina de Facebook o Twitter).'
    }
    
    step = forms.IntegerField(widget=forms.HiddenInput, initial=1)
    nombre = forms.CharField(help_text=ayudas['nombre'],widget=forms.TextInput(attrs={'class':'input-text'}))
    domicilio = forms.CharField(help_text=ayudas['domicilio'],widget=forms.TextInput(attrs={'class':'input-text'}))
    telefono = forms.CharField(help_text=ayudas['telefono'],label=u'Tel\xe9fono', widget=forms.TextInput(attrs={'class':'input-text'}), required=False)
    celular = forms.CharField(help_text=ayudas['celular'],widget=forms.TextInput(attrs={'class':'input-text'}), required=False)
    mail = forms.CharField(help_text=ayudas['mail'],widget=forms.TextInput(attrs={'class':'input-text'}))
    descripcion = forms.CharField(help_text=ayudas['descripcion'],
                                  label=u"Descripci\xf3n", 
                                  required=False, 
                                  widget=forms.Textarea(attrs = 
                                                        {'class':'txt-area', 
                                                         'cols': '35', 'rows': '5'}))
    tipo = forms.ChoiceField(help_text=ayudas['tipo'],choices=UserProfile.TIPO_EMPRESA)
    documento = forms.CharField(help_text=ayudas['documento'],widget=forms.TextInput(attrs={'class':'input-text'}), required=False)
    web = forms.CharField(help_text=ayudas['web'],widget=forms.TextInput(attrs={'class':'input-text'}), required=False)


    class Meta:
        model = UserProfile
        fields = ('nombre', 'domicilio', 'telefono', 'celular', 
                  'mail', 'descripcion', 'logo', 'documento', 'tipo', 'web')
    