from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def show_main(request):
    notes = Note.objects.all()
    tags = Tag.objects.all()
    note_has_tag = NoteHasTag.objects.all()
    response = render(request, 'evernote/main.html', {'notes': notes, 'tags': tags, 'note_has_tag' : note_has_tag})
    return HttpResponse(response)


def landing(request):
    response = render_to_string('evernote/index.html')
    return HttpResponse(response)


def registration(request):
    response = render_to_string('evernote/registration.html')
    return HttpResponse(response)
