from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView  # temporal
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Rubro
from .forms import AltaUsuarioForm, UsuarioInlineFormSet#, seleccion_rubro

# IMPORTANTE: los usuarios nunca publican, solo agregan servicios, el mensaje:
# "Publicar" en la web es lo mismo que Alta de usuario.

class CrearUsuarioView(CreateView):
    template_name = 'usuarios/crear-usuario.html'
    model = User
    form_class = AltaUsuarioForm # the parent object's form

    # On successful form submission
    def get_success_url(self):
        return reverse('usuario-creado')

    # Validate forms
    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save() # saves Father and Children
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    # We populate the context with the forms. Here I'm sending
    # the inline forms in `inlines`
    def get_context_data(self, **kwargs):
        ctx = super(CrearUsuarioView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = AltaUsuarioForm(self.request.POST)
            ctx['servicio_inlines'] = UsuarioInlineFormSet(self.request.POST)
        else:
            ctx['form'] = AltaUsuarioForm()
            ctx['servicio_inlines'] = UsuarioInlineFormSet()
            #ctx['select_rubros'] = seleccion_rubro
            
        return ctx
    
    
class ModificarView(TemplateView):
    template_name = 'usuarios/modificar.html'
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        ret = super(ModificarView, self).get(request, *args, **kwargs)
        return ret
        
