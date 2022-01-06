from django import forms
from .models import *


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'noteTitle', 'placeholder': 'Новая заметка'}),
            'text': forms.Textarea(
                attrs={'class': 'noteBody', 'cols': 100, 'rows': 20, 'placeholder': 'Текст заметки'}),
        }


class AddTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'noteTags'}),
        }


class FilterForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'filterForms'}), required=False,
                           label='По дате')
    tag = forms.CharField(widget=forms.TextInput(attrs={'class': 'filterForms'}), max_length=45, required=False,
                          label='По тегу')
