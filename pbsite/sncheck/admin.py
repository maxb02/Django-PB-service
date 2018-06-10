from django.contrib import admin
from .models import EmailForNotifications, AllowedDeviceRegion, SerialNumberCheckJournal


@admin.register(EmailForNotifications)
class EmailForNotificationsAdmin(admin.ModelAdmin):
    list_display = ('user_region', 'email')
    list_filter = ('user_region', 'email')


@admin.register(AllowedDeviceRegion)
class AllowedDeviceRegionAdmin(admin.ModelAdmin):
    list_display = ('device_region', 'user_region',)
    list_filter = ('user_region', 'device_region')


@admin.register(SerialNumberCheckJournal)
class Serial_Number_Check_JournalAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'user', 'is_valid', 'is_region_match', 'date')
    list_filter = ('date', 'user', 'is_valid', 'is_region_match',)
    search_fields = ('serial_number',)
