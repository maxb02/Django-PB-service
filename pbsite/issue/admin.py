from django.contrib import admin
from .models import BatteryIssue

@admin.register(BatteryIssue)
class BattereIssueAdmin(admin.ModelAdmin):
    list_display = 'id', 'device_serial_number', 'user', 'filling_date'
    search_fields = 'id', 'device_serial_number',

