from django.contrib import admin
from .models import Device
from .models import Guide
from .models import News
from reversion.admin import VersionAdmin

class GuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'device', 'updated_date')
    list_filter = ('device', 'updated_date', )

@admin.register(Guide)
class YourModelAdmin(VersionAdmin, GuideAdmin):
    pass

# @admin.register(Device)
# class Device(VersionAdmin):
#     pass

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','type', 'published_date')
    list_filter = ('type', 'published_date')

@admin.register(News)
class YourModelAdmin(VersionAdmin, NewsAdmin):
    pass

@admin.register(Device)
class YourModelAdmin(VersionAdmin):
    pass

# admin.site.register(Device)
# admin.site.register(Guide, GuideAdmin)
