from django.contrib import admin
from .models import BatteryIssue

@admin.register(BatteryIssue)
class BattereIssueAdmin(admin.ModelAdmin):
    pass

