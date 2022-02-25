from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import generics, status, mixins
from rest_framework.renderers import StaticHTMLRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from . import serializers
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


class NotesAPIList(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('-date')
    serializer_class = serializers.NoteSerializer

    def perform_create(self, serializer):
        serializer.save(person=self.request.user)


class TagAPICreate(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class NoteAPIUpdate(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer


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


class NoteViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer



class New_Note(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'evernote/new_note.html'

    def post(self, request):
        serializer = serializers.NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def download_file(request, idnote: int):
    file = Note.objects.get(pk=idnote).file
    response = HttpResponse(file)
    filename = str(file).rsplit('/', 1)[1]
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response


def deletenote_page(request, idnote: int):
    if request.user.is_authenticated:
        Note.objects.get(pk=idnote).delete()
        response = {
            'success': 'true',
        }
        return JsonResponse(response)


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


class New_Tag(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'evernote/new_tag.html'

    def post(self, request):
        serializer = serializers.TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# def landing(request):
#     response = render(request, 'evernote/index.html')
#     return HttpResponse(response)


class Landing(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'evernote/index.html'

    def get(self, request):
        return Response()


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
