from django.template.loader import render_to_string
from django.http import HttpResponse

def show_main(request):
    responce = render_to_string('evernote/main.html')
    return HttpResponse(responce)


def landing(request):
    responce = render_to_string('evernote/index.html')
    return HttpResponse(responce)


def registration(request):
    responce = render_to_string('evernote/registration.html')
    return HttpResponse(responce)
