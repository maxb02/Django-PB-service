from django.contrib import admin
from .models import Device
from .models import Guide
from .models import News
from reversion.admin import VersionAdmin

@admin.register(Guide)
class Guide(VersionAdmin):
    pass

@admin.register(Device)
class Device(VersionAdmin):
    pass

@admin.register(News)
class News(VersionAdmin):
    pass



# admin.site.register(Device)
# admin.site.register(Guide)
