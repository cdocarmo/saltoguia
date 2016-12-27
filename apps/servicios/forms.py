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
    
    ayudas = {
              'nombre':u'Un nombre que describa el servicio, por ej: "Reparaci\xf3n de pc\'s".',
              'descripcion':u'Una descripci\xf3n mas detallada.',
              'tags':u'Una lista de palabras claves separadas por como, por ej: "reparacion, pc, notebook, formateo".'
    }
    
    empresa_id = forms.CharField(widget=forms.HiddenInput)     
    step = forms.IntegerField(widget=forms.HiddenInput, initial=2)
    nombre_servicio = forms.CharField(label=u"Nombre del servicio",
                                      widget=forms.TextInput(attrs={'class':'input-text'}), 
                                      help_text=ayudas['nombre'], required=True) 
    desc_servicio = forms.CharField(label=u"Descripci\xf3n", 
                                  required=True, 
                                  widget=forms.Textarea(attrs = 
                                                        {'class':'txt-area', 
                                                         'cols': '40', 'rows': '5'}),
                                  help_text = ayudas['descripcion'])   
    tags = forms.CharField(label=u"Tags", required=True, widget=forms.Textarea(attrs={'class':'txt-area', 'cols':'40', 'rows':'5'}),
                           help_text=ayudas['tags'])      
    
    def as_br(self):
        """
        GF
        Based in as_p, from superclass forms.py.
        Returns this form rendered as HTML <br />s.
        """
        return self._html_output(
            normal_row = u'%(label)s <br />%(field)s<br />',
            error_row = u'%s',
            row_ender = '',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)
    
    class Meta:
        model = Servicio
        fields = ('nombre_servicio', 'desc_servicio', 'tags',)
        

class Modificar_ServicioForm(forms.Form):

   
    
    def __init__(self, *args, **kwargs):        
        super(Modificar_ServicioForm, self).__init__(*args, **kwargs)
    