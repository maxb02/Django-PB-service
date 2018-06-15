from django.contrib import admin
from .models import Device
from .models import Guide
from reversion.admin import VersionAdmin

@admin.register(Guide)
class GuideAdmin(VersionAdmin):
    list_display = ('title', 'device', 'updated_date')
    list_filter = ('device', 'updated_date', )

@admin.register(Device)
class DeviceAdmin(VersionAdmin):
    pass