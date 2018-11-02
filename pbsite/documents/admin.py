from django.contrib import admin
from .models import Act, SerialNumberPrefix, VisualDefect, Accessory

@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    pass


@admin.register(SerialNumberPrefix)
class SerialNumberPrefixAdmin(admin.ModelAdmin):
    pass

@admin.register(VisualDefect)
class VisualDefectAdmin(admin.ModelAdmin):
    pass

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    pass