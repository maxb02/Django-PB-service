from django.db import models
from django.contrib.auth.models import Group
from ckeditor_uploader.fields import RichTextUploadingField


class NewsManager(models.Manager):
    def for_user_groups(self, user):
        return self.order_by('-published_date').filter(group=user.groups.all())


class News(models.Model):
    group = models.ManyToManyField(Group)
    type = models.CharField(max_length=50, choices=(
        ('alert alert-primary', "primary"),
        ('alert alert-success', "success"),
        ('alert alert-danger', "danger"),
        ('alert alert-warning', "warning"),
        ('alert alert-info', "info"),
        ('alert alert-light', "light"),
        ('alert alert-dark', "dark"),
    ))
    title = models.CharField(max_length=200)
    text = RichTextUploadingField('contents')
    published_date = models.DateTimeField(blank=True, auto_now=True)

    objects = NewsManager()

    def __str__(self):
        return self.title
