from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=25)
    model_number = models.CharField(max_length=10)
    serial_number_prefix = models.CharField(max_length=3)
    image = models.ImageField(upload_to='device')

    def __str__(self):
        return self.name
