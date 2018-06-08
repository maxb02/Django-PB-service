from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import ServiceCenter

admin.site.register(ServiceCenter)
