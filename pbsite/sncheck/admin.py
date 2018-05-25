from django.contrib import admin
from .models import EmailForNotifications
from .models import AllowedDeviceRegion

admin.site.register(EmailForNotifications)


class AllowedDeviceRegionAdmin(admin.ModelAdmin):
    list_display = ('device_region', 'user_region',)
    list_filter = ('user_region', 'device_region')


@admin.register(AllowedDeviceRegion)
class YourModelAdmin(AllowedDeviceRegionAdmin):
    pass