from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import EmailForNotifications, AllowedDeviceRegion, SerialNumberCheckJournal


@admin.register(EmailForNotifications)
class EmailForNotificationsAdmin(admin.ModelAdmin):
    list_display = ('user_region', 'email')
    list_filter = ('user_region', 'email')


@admin.register(AllowedDeviceRegion)
class AllowedDeviceRegionAdmin(admin.ModelAdmin):
    list_display = ('device_region', 'user_region',)
    list_filter = ('user_region', 'device_region')


class SerialNumberCheckJournalResource(resources.ModelResource):
    class Meta:
        model = SerialNumberCheckJournal
        fields = (
        'serial_number', 'user__username', 'user__service_center__company_name', 'date', 'is_valid', 'is_region_match')


@admin.register(SerialNumberCheckJournal)
class Serial_Number_Check_JournalAdmin(ImportExportModelAdmin):
    resource_class = SerialNumberCheckJournalResource
    list_display = ('serial_number', 'user', 'is_valid', 'is_region_match', 'date')
    list_filter = ('date', 'user', 'is_valid', 'is_region_match',)
    search_fields = ('serial_number',)
