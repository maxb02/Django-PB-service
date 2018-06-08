from django.db import models
from django.contrib.auth.models import Group, User
from django.conf import settings

class EmailForNotifications(models.Model):
    email = models.EmailField()
    user_region = models.ForeignKey(Group, null=True)

    def __str__(self):
        return self.email

class AllowedDeviceRegion(models.Model):
    user_region = models.ForeignKey(Group, null=True)
    device_region = models.CharField(max_length=200)

    def __str__(self):
        return self.device_region

class SerialNumberCheckJournal(models.Model):
    serial_number = models.CharField(max_length=50, verbose_name ='Serial Number')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, verbose_name ='User Name')
    is_valid = models.NullBooleanField(verbose_name ='SN is valid')
    is_region_match = models.NullBooleanField('Region Match')
    date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.serial_number



