from django.db import models
from django.contrib.auth.models import Group


class Guide(models.Model):
    title = models.CharField(max_length=50)
    device = models.ForeignKey('technicalguides.Device', related_name='guide', on_delete=models.CASCADE)
    group = models.ManyToManyField(Group, related_name='guides')


class Step(models.Model):
    guide = models.ForeignKey('Guide', related_name='step', on_delete=models.CASCADE)
    text = models.TextField()


class Notice(models.Model):
    step = models.ForeignKey('Step', related_name='notice', on_delete=models.CASCADE)
    text = models.TextField()


class Image(models.Model):
    step = models.ForeignKey('Step', related_name='image', on_delete=models.CASCADE)
    image = models.ImageField()


class File(models.Model):
    step = models.ForeignKey('Step', related_name='file', on_delete=models.CASCADE)
    file = models.FileField()


class Link(models.Model):
    step = models.ForeignKey('Step', related_name='link', on_delete=models.CASCADE)
    link = models.URLField()
