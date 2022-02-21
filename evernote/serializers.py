from rest_framework import serializers
from django.contrib.auth.models import User
from evernote.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class NoteHasTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteHasTag
        fields = ('id', 'note', 'tag',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'person', 'name', 'date', 'text', 'file',)
