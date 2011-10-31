# coding=UTF-8

from django import forms
from searchs.models import Searchs

class SearchForm(forms.ModelForm):
    
    search_word = forms.CharField(widget=forms.TextInput(attrs={'id':'search-box', 'class':'input-text'}))
    class Meta:
        model = Searchs
        fields = ('search_word',)