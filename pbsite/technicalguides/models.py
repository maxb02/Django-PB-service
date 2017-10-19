from django.db import models
from django.contrib.auth.models import Group
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

class Device(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='device')

    def add(self):
        self.save()

    def __str__(self):
        return self.name


class Guide(models.Model):
    title = models.CharField(max_length=200)
    device = models.ForeignKey(Device, blank=True)
    group = models.ManyToManyField(Group)
    text = RichTextUploadingField('contents')
    published_date = models.DateTimeField(blank=True, auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return self.title


class News(models.Model):
    group = models.ManyToManyField(Group)
    type = models.CharField(max_length=50, choices=(
        ('alert alert-primary', "primary"),
        ('alert alert-success', "success"),
        ('alert alert-danger', "danger"),
        ('alert alert-warning', "warning"),
        ('alert alert-info', "info" ),
        ('alert alert-light', "light"),
        ('alert alert-dark', "dark"),
    ))
    title = models.CharField(max_length=200)
    text = RichTextUploadingField('contents')
    published_date = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return self.title


class Procedure(models.Model):
    group = models.ManyToManyField(Group)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField('contents')
    published_date = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return self.title