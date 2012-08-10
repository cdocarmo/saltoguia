from django import forms
from django.utils.translation import ugettext_lazy as _, ungettext
from empresa.models import Empresa, EmpresaServicio
from django.utils.translation import ugettext as _
from utilita.thumbs import ImageWithThumbsField

class EmpresaForm(forms.ModelForm):
    
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
    tipo = forms.ChoiceField(help_text=ayudas['tipo'],choices=Empresa.TIPO_EMPRESA)
    documento = forms.CharField(help_text=ayudas['documento'],widget=forms.TextInput(attrs={'class':'input-text'}), required=False)
    web = forms.CharField(help_text=ayudas['web'],widget=forms.TextInput(attrs={'class':'input-text'}), required=False)


    class Meta:
        model = Empresa
        fields = ('nombre', 'domicilio', 'telefono', 'celular', 
                  'mail', 'descripcion', 'logo', 'documento', 'tipo', 'web')

class Empresa_ServicioForm(forms.ModelForm):
    """
    forms.ModelForm ---> cuando va a ser un formulario en base a un modelo
    forms.Form ---> cuando es un formulario creado y recibe parametros
    
        """
    empresa_id = forms.CharField(widget=forms.HiddenInput)     
    step = forms.IntegerField(widget=forms.HiddenInput, initial=2)
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}), required=True) 
    descripcion = forms.CharField(label=u"Descripci\xf3n", 
                                  required=True, 
                                  widget=forms.Textarea(attrs = 
                                                        {'class':'txt-area', 
                                                         'cols': '35', 'rows': '5'}))   
    tags = forms.CharField(label="Tags", 
                          required=True, 
                          widget=forms.Textarea(attrs = 
                                                {'class':'txt-area', 
                                                 'cols': '35', 'rows': '5'}))      
    class Meta:
        model = EmpresaServicio
        fields = ('nombre', 'descripcion', 'tags' )
        

class Modificar_ServicioForm(forms.Form):

   
    
    def __init__(self, *args, **kwargs):        
        super(Modificar_ServicioForm, self).__init__(*args, **kwargs)
    