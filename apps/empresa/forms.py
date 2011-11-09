from django import forms
from django.utils.translation import ugettext_lazy as _, ungettext
from empresa.models import Empresa, EmpresaServicio
from django.utils.translation import ugettext as _

class EmpresaForm(forms.ModelForm):
    step = forms.IntegerField(widget=forms.HiddenInput, initial=1)
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}))
    domicilio = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}))
    celular = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}))
    mail = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text'}))
    descripcion = forms.CharField(label="Descripcion", required=False, widget=forms.Textarea(attrs = {'class':'txt-area', 'cols': '35', 'rows': '5'}))
    
    def clean_name(self):
        if Empresa.objects.filter(name__iexact=self.cleaned_data["nombre"]).count() > 0:
            if self.cleaned_data["nombre"] == self.instance.name:
                pass # same instance
            else:
                raise forms.ValidationError(_("Ya existe la empresa con ese Nombre"))
        return self.cleaned_data["nombre"]

    class Meta:
        model = Empresa
        fields = ('nombre', 'domicilio', 'telefono', 'celular', 'mail', 'descripcion', )

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
