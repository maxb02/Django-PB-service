from django.contrib import admin
from .models import News
from reversion.admin import VersionAdmin

@admin.register(News)
class YourModelAdmin(VersionAdmin):
    list_display = ('title', 'type', 'published_date')
    list_filter = ('type', 'published_date')