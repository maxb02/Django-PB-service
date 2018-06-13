from django.contrib.auth.models import AbstractUser
from django.db import models
from servicecenters.models import ServiceCenter

class User(AbstractUser):
    service_center = models.ForeignKey(ServiceCenter, blank=True, null=True)
    class Meta:
        db_table = 'auth_user'
