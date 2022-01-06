from django import forms
from .models import *


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'text']


class AddTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class FilterForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'filterForms'}), required=False,
                           label='По дате')
    tag = forms.CharField(widget=forms.TextInput(attrs={'class': 'filterForms'}), max_length=45, required=False,
                          label='По тегу')
