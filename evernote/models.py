from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Note(models.Model):
    person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=45, null=False)
    date = models.DateField(auto_now=True, null=False)
    text = models.TextField(null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.name


class NoteHasTag(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, null=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=False)
