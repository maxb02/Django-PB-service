from django.db import models
from django.urls import reverse

class Device(models.Model):
    name = models.CharField(max_length=25, unique=True)
    model_number = models.CharField(max_length=10, unique=True)
    serial_number_prefix = models.CharField(max_length=3, null=True, blank=True)
    image = models.ImageField(upload_to='device')

    def get_absolute_url(self):
        return reverse('device_detail_url', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
