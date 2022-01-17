from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class BinaryFileInput(forms.ClearableFileInput):
    def is_initial(self, value):
        return bool(value)

    def format_value(self, value):
        if self.is_initial(value):
            return f'{len(value)} bytes'

    def value_from_datadict(self, data, files, name):
        upload = super().value_from_datadict(data, files, name)
        if upload:
            return upload.read()


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'text', 'file')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'noteTitle', 'placeholder': 'Новая заметка'}),
            'text': forms.Textarea(
                attrs={'class': 'noteBody', 'cols': 100, 'rows': 20, 'placeholder': 'Текст заметки'}),
            'file': BinaryFileInput(attrs={'style': 'position: absolute; z-index: -1; opacity: 0; overflow: hidden;'})
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


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'loginForm', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'loginForm', 'placeholder': 'Пароль'}))

    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'loginForm', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'loginForm', 'placeholder': 'Username'}),
        }


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'regForm', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'regForm', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'regForm', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'regForm', 'placeholder': 'Фамилия'}),
            'username': forms.TextInput(attrs={'class': 'regForm', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'regForm', 'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'regForm', 'placeholder': 'Подтвердите пароль'}),
        }
        help_texts = {
            'username': '',
            'password1': '',
            'password2': '',
        }
