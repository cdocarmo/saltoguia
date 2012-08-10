from django import forms
from django.utils.translation import ugettext_lazy as _, ungettext
from servicios.models import Servicio
from django.utils.translation import ugettext as _
from utilita.thumbs import ImageWithThumbsField



class ServicioForm(forms.ModelForm):
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
        model = Servicio
        fields = ('nombre', 'descripcion', 'tags' )
        

class Modificar_ServicioForm(forms.Form):

   
    
    def __init__(self, *args, **kwargs):        
        super(Modificar_ServicioForm, self).__init__(*args, **kwargs)
    