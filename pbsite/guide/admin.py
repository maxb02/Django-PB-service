from django.contrib import admin
from .models import Guide
from reversion.admin import VersionAdmin


@admin.register(Guide)
class GuideAdmin(VersionAdmin):
    list_display = ('title', 'device',)
