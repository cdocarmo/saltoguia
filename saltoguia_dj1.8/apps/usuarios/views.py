from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import AltaUsuarioForm, UsuarioInlineFormSet


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
            ctx['inlines'] = UsuarioInlineFormSet(self.request.POST)
        else:
            ctx['form'] = AltaUsuarioForm()
            ctx['inlines'] = UsuarioInlineFormSet()
        return ctx
