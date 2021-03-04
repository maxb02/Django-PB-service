from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from device.models import Device as NewDevice


class Device(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='device')

    def add(self):
        self.save()

    def __str__(self):
        return self.name


class GuideManager(models.Manager):
    def for_user_groups(self, user):
        return self.order_by('-updated_date').filter(group=user.groups.all())


class Guide(models.Model):
    title = models.CharField(max_length=200)
    device = models.ForeignKey(Device)
    group = models.ManyToManyField(Group)
    text = RichTextUploadingField('contents')
    published_date = models.DateTimeField(blank=True, auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, auto_now=True)
    objects = GuideManager()
    new_device = models.ForeignKey(NewDevice, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('technocalguide_by_pk_detail_url', kwargs={'pk': self.pk})


# Fake file FileBrowser model
class FileBrowser(models.Model):
    class Meta:
        managed = False
        verbose_name = _('FileBrowser')
        verbose_name_plural = _('FileBrowser')