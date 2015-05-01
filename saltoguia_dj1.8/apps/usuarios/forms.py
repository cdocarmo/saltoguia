# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import Servicio, Rubro, SubRubro, Area



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
    qset_areas = Area.objects.all()
    AREAS = ( (sr.pk, sr.nombre) for sr in qset_areas )
    
    first_name = forms.CharField(label=u'Nombres')
    last_name = forms.CharField(label=u'Apellidos')
    email = forms.CharField(label=u'Email')
    categoria = forms.ChoiceField(label=u'Categoría', choices=AREAS)
    avatar = forms.ImageField(label=u'Avatar')
    domicilio = forms.CharField(label=u'Domicilio')
    horarios = forms.CharField(label=u'Horarios de disponibilidad')
    dias_habiles = forms.CharField(label=u'Días de atención')
    aclaraciones = forms.CharField(label=u'Comentarios')
    
    
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'categoria', 'avatar', 'domicilio', 'horarios', 'dias_habiles', 'aclaraciones')
        
        
class AltaServicioInlineForm(forms.ModelForm):
    qset_subrubros = SubRubro.objects.all()
    SUBRUBROS = ( (sr.pk, sr.nombre) for sr in qset_subrubros )
    
    qset_rubros = Rubro.objects.all()
    RUBROS = ( (sr.pk, sr.nombre) for sr in qset_rubros )
    
    descripcion = forms.CharField(label=u'Descripción')
    telefono = forms.CharField(label=u'Teléfono particular para solicitar el servicio')  # max_length=16
    rubro = forms.ChoiceField(widget=forms.Select, choices=RUBROS)
    subrubro = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SUBRUBROS)
    
    class Meta:
        model = Servicio
        fields = ('descripcion', 'telefono', 'rubro', 'subrubro',)
        
        
        
UsuarioInlineFormSet = forms.inlineformset_factory(User,
    Servicio,
    form=AltaServicioInlineForm,
    extra=1
)



