from django import forms
from django.utils.translation import ugettext_lazy as _, ungettext
from empresas.models import Empresa
from django.utils.translation import ugettext as _


class EmpresaForm(forms.ModelForm):
    descipcion = forms.CharField(label="Description", required=False, widget=forms.Textarea(attrs = {'cols': '35', 'rows': '5'}))

    def clean_name(self):
        if Empresa.objects.filter(name__iexact=self.cleaned_data["nombre"]).count() > 0:
            if self.cleaned_data["nombre"] == self.instance.name:
                pass # same instance
            else:
                raise forms.ValidationError(_("Ya existe la empresa con ese Nombre"))
        return self.cleaned_data["nombre"]

    class Meta:
        model = Empresa
        fields = ('nombre', 'domicilio', 'telefono', 'celular', 'mail', 'descipcion', )
