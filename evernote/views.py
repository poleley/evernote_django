from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        add_note = AddNoteForm(request.POST)
        if add_note.is_valid():
            add_note.save()
            return redirect('main_page')
    else:
        add_note = AddNoteForm()
    data = {'add_note': add_note}
    return render(request, 'evernote/new_note.html', data)


def new_tag(request):
    add_tag = AddTagForm()
    data = {'add_tag': add_tag}
    return render(request, 'evernote/new_tag.html', data)


def landing(request):
    response = render(request, 'evernote/index.html')
    return HttpResponse(response)


def registration(request):
    response = render(request, 'evernote/registration.html')
    return HttpResponse(response)


def login(request):
    response = render(request, 'evernote/login.html')
    return HttpResponse(response)
