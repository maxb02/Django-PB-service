from django.db import models
from django.urls import reverse


class Factory(models.Model):
    name = models.CharField(max_length=25, unique=True)
    code = models.CharField(max_length=2, unique=True, db_index=True)

    def __str__(self):
        return '{} | {}'.format(self.name, self.code)


class Module(models.Model):
    name = models.CharField(max_length=25, unique=True)
    code = models.CharField(max_length=2, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} | {}'.format(self.name, self.code)


class Region(models.Model):
    name = models.CharField(max_length=25, unique=True)
    code = models.CharField(max_length=1, unique=True, db_index=True)

    def __str__(self):
        return '{} | {}'.format(self.name, self.code)


class Project(models.Model):
    name = models.CharField(max_length=35, unique=True)
    code = models.CharField(max_length=3, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} | {}'.format(self.name, self.code)


class Color(models.Model):
    name = models.CharField(max_length=25, unique=True)
    code = models.CharField(max_length=1, unique=True, db_index=True)

    def __str__(self):
        return '{} | {}'.format(self.name, self.code)


class Device(models.Model):
    name = models.CharField(max_length=25, unique=True)
    model_number = models.CharField(max_length=10, unique=True)
    serial_number_prefix = models.CharField(max_length=3, null=True, blank=True)
    image = models.ImageField(upload_to='device')
    code = models.CharField(max_length=1, null=True, db_index=True)
    factory = models.ForeignKey(Factory, null=True, related_name='devices')

    class Meta:
        unique_together = ('model_number', 'code')

    def get_absolute_url(self):
        return reverse('device_detail_url', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} | {}'.format(self.name, self.code)


class SKU(models.Model):
    name = models.CharField(max_length=25, unique=True)
    region = models.ForeignKey(Region, related_name='skus', null=False, blank=False)
    project = models.ForeignKey(Project, related_name='skus', null=False, blank=False)
    color = models.ForeignKey(Color, related_name='skus', null=False, blank=False)
    module = models.ForeignKey(Module, related_name='skus', null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    device = models.ForeignKey(Device, related_name='skus', null=False, blank=False)

    def __str__(self):
        return self.name
