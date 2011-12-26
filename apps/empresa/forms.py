from django import forms
from django.utils.translation import ugettext_lazy as _, ungettext
from empresa.models import Empresa, EmpresaServicio
from django.utils.translation import ugettext as _
from utilita.thumbs import ImageWithThumbsField

class EmpresaForm(forms.ModelForm):
    step = forms.IntegerField(widget=forms.HiddenInput, initial=1)
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}))
    domicilio = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}), required=False)
    celular = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}), required=False)
    mail = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}))
    descripcion = forms.CharField(label="Descripcion", 
                                  required=False, 
                                  widget=forms.Textarea(attrs = 
                                                        {'class':'txt-area', 
                                                         'cols': '35', 'rows': '5'}))
    tipo = forms.ChoiceField(choices=Empresa.TIPO_EMPRESA)
    documento = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}), required=False)
    web = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}), required=False)


    class Meta:
        model = Empresa
        fields = ('nombre', 'domicilio', 'telefono', 'celular', 
                  'mail', 'descripcion', 'logo', 'documento', 'tipo', 'web')

class Empresa_ServicioForm(forms.ModelForm):
    """
    forms.ModelForm ---> cuando va a ser un formulario en base a un modelo
    forms.Form ---> cuando es un formulario creado y recibe parametros
    
        """
    empresa_id = forms.ModelChoiceField(Empresa.objects.all(), widget=forms.HiddenInput)        
    step = forms.IntegerField(widget=forms.HiddenInput, initial=2)
    class Meta:
        model = EmpresaServicio
        fields = ('nombre', 'descripcion', 'tags' )
