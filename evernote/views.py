from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def show_main(request):
    notes = Note.objects.all()
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


def new_note(request):
    add_note = AddNoteForm()
    data = {'add_note': add_note}
    return render(request, 'evernote/new_note.html')


def landing(request):
    response = render(request, 'evernote/index.html')
    return HttpResponse(response)


def registration(request):
    response = render(request, 'evernote/registration.html')
    return HttpResponse(response)


def login(request):
    response = render(request, 'evernote/login.html')
    return HttpResponse(response)
