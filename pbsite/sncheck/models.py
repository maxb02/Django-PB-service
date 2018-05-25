from django.db import models
from django.contrib.auth.models import Group

class EmailForNotifications(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class AllowedDeviceRegion(models.Model):
    user_region = models.ForeignKey(Group, null=True)
    device_region = models.CharField(max_length=200)

    def __str__(self):
        return self.device_region

