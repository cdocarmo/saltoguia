from django import forms
from django.contrib.auth.models import User
from .models import Servicio



class AltaUsuarioForm(forms.ModelForm):
    """
    forms.ModelForm ---> cuando va a ser un formulario en base a un modelo
    forms.Form ---> cuando es un formulario creado y recibe parametros
    
    """
    
    #ayudas = {
    #          'nombre':u'Un nombre que describa el servicio, por ej: "Reparaci\xf3n de pc\'s".',
    #          'descripcion':u'Una descripci\xf3n mas detallada.',
    #          'tags':u'Una lista de palabras claves separadas por como, por ej: "reparacion, pc, notebook, formateo".'
    #}
    
    #empresa_id = forms.CharField(widget=forms.HiddenInput)     
    #step = forms.IntegerField(widget=forms.HiddenInput, initial=2)
    #nombre_servicio = forms.CharField(label=u"Nombre del servicio",
    #                                  widget=forms.TextInput(attrs={'class':'input-text'}), 
    #                                  help_text=ayudas['nombre'], required=True) 
    #desc_servicio = forms.CharField(label=u"Descripci\xf3n", 
    #                              required=True, 
    #                              widget=forms.Textarea(attrs = 
    #                                                    {'class':'txt-area', 
    #                                                     'cols': '40', 'rows': '5'}),
    #                              help_text = ayudas['descripcion'])   
    #tags = forms.CharField(label=u"Tags", required=True, widget=forms.Textarea(attrs={'class':'txt-area', 'cols':'40', 'rows':'5'}),
    #                       help_text=ayudas['tags'])
    
    first_name = forms.CharField(label=u'Nombres')
    last_name = forms.CharField(label=u'Apellidos')
    email = forms.CharField(label=u'Email')
    categoria = forms.ChoiceField(label=u'Categor&iacute;a')
    avatar = forms.ImageField(label=u'Avatar')
    domicilio = forms.CharField(label=u'Domicilio')
    horarios = forms.CharField(label=u'Horarios de disponibilidad')
    dias_habiles = forms.CharField(label=u'D&iacute;as de atenci&oacute;n')
    aclaraciones = forms.CharField(label=u'Comentarios')
    
    
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'categoria', 'avatar', 'domicilio', 'horarios', 'dias_habiles', 'aclaraciones')
        
        
class AltaServicioInlineForm(forms.ModelForm):
    
    descripcion = forms.CharField(label=u'Descripci&oacute;n')
    telefono = forms.CharField(label=u'Tel&eacute;fono particular para solicitar el servicio')  # max_length=16
    
    class Meta:
        model = Servicio
        fields = ('descripcion', 'telefono',)
        
        
UsuarioInlineFormSet = forms.inlineformset_factory(User,
    Servicio,
    form=AltaServicioInlineForm,
    extra=1,
    can_delete=False,
    can_order=False
)