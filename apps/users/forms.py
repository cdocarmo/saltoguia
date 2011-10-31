# coding=UTF-8
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    usuario = forms.CharField(label=_(u'Usuario'), max_length=100)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)




class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ("username", "email", )