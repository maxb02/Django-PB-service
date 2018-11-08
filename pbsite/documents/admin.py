from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Act, SerialNumberPrefix, VisualDefect, Accessory

@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    pass


@admin.register(SerialNumberPrefix)
class SerialNumberPrefixAdmin(admin.ModelAdmin):
    pass


class AccessoryAdmin(TranslationAdmin):
    pass
admin.site.register(Accessory, AccessoryAdmin)

class VisualDefectAdmin(TranslationAdmin):
    pass

admin.site.register(VisualDefect, VisualDefectAdmin)