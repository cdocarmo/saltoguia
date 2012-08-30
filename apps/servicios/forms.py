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
        model = Servicio
        fields = ('nombre', 'descripcion', 'tags' )
        

class Modificar_ServicioForm(forms.Form):

   
    
    def __init__(self, *args, **kwargs):        
        super(Modificar_ServicioForm, self).__init__(*args, **kwargs)
    