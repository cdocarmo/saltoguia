# coding=UTF-8
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms
# from django.contrib.auth.models import User
from datetime import date, datetime, timedelta
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    usuario = forms.CharField(label=_(u'Usuario'), max_length=100, 
                              widget=forms.TextInput(attrs={'class':'input-text'}))
    password = forms.CharField(label=_(u'Password'), 
                               widget=forms.PasswordInput(attrs={'class':'input-text'}))

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


class RegisterForm(UserCreationForm):
    username = forms.CharField(label=_(u'*Usuario'), max_length=30, widget=forms.TextInput(attrs={'class':'input-text'}))
    email = forms.EmailField(label = "*Email", widget=forms.TextInput(attrs={'class':'input-text'}))
    #override password1 and password2 from UserCreationForm
    password1 = forms.CharField(label=_("*Password"), widget=forms.PasswordInput(attrs={'class':'input-text'}))
    password2 = forms.CharField(label=_("*Password confirmation"), widget=forms.PasswordInput(attrs={'class':'input-text'}),
        help_text = _("Enter the same password as above, for verification."))
    validation = forms.BooleanField(label="*Validacion", widget=forms.CheckboxInput(), help_text = "Acepto que estos datos \
        sean almacenados en la base de datos de saltoguia.com.uy. (Estos datos pueden ser elimnados en el momento que usted desee.)")
    
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
        model = User
        fields = ("username", "email", )

