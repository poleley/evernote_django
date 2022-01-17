from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import *


def show_main(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(person_id=request.user.id).order_by('-date')
        tags = Tag.objects.all()
        note_has_tag = NoteHasTag.objects.all()
        data = {'notes': notes, 'tags': tags, 'note_has_tag': note_has_tag}
        if request.method == 'POST':
            filter_form = FilterForm(request.POST)
            if filter_form.is_valid():
                if filter_form.cleaned_data['date'] is not None:
                    notes = notes.filter(date=filter_form.cleaned_data['date'])
                if filter_form.cleaned_data['tag'] != '':
                    notes = notes.filter(notehastag__tag__name=filter_form.cleaned_data['tag'])
                data['notes'] = notes
        else:
            filter_form = FilterForm()
        data['filter_form'] = filter_form
        return render(request, 'evernote/main.html', data)
    else:
        return redirect('registration_page')


def new_note(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            add_note = AddNoteForm(request.POST, request.FILES)
            if add_note.is_valid():
                added_note = add_note.save()
                added_note.person = request.user
                added_note.save()
                return redirect('main_page')
        else:
            add_note = AddNoteForm()
        data = {'add_note': add_note}
        return render(request, 'evernote/new_note.html', data)
    else:
        return redirect('registration_page')


def deletenote_page(request, idnote: int):
    if request.user.is_authenticated:
        note = Note.objects.get(pk=idnote)
        note.delete()
        return redirect('main_page')
    else:
        return redirect('registration_page')


def new_tag(request, idnote: int):
    if request.user.is_authenticated:
        if request.method == 'POST':
            add_tag = AddTagForm(request.POST)
            if add_tag.is_valid():
                added_tag = add_tag.save()
                note_has_tag = NoteHasTag(note_id=idnote, tag_id=added_tag.id)
                note_has_tag.save()
            return redirect('main_page')
        else:
            add_tag = AddTagForm()
        data = {'add_tag': add_tag, 'idnote': idnote}
        return render(request, 'evernote/new_tag.html', data)
    else:
        return redirect('registration_page')


def landing(request):
    response = render(request, 'evernote/index.html')
    return HttpResponse(response)


def logout_user(request):
    logout(request)
    return redirect('landing_page')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'evernote/login.html'

    def get_success_url(self):
        return reverse_lazy('main_page')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'evernote/registration.html'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main_page')

