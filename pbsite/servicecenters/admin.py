from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import ServiceCenter

@admin.register(ServiceCenter)
class ServiceCenterAdmin(VersionAdmin):
    list_display = ('company_name', 'region', 'language', 'country', 'city')
    list_filter = ('region', 'language', 'country')