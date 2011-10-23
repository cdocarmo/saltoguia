# coding=UTF-8

from django import forms
from searchs.models import Searchs

class SearchForm(forms.ModelForm):
    class Meta:
        model = Searchs
        fields = ('search_word',)