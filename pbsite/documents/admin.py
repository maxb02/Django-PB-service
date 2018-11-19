from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Act, SerialNumberPrefix, VisualDefect, ScopeOfSupply

@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    pass


@admin.register(SerialNumberPrefix)
class SerialNumberPrefixAdmin(admin.ModelAdmin):
    pass


class ScopeOfSupplyAdmin(TranslationAdmin):
    pass
admin.site.register(ScopeOfSupply, ScopeOfSupplyAdmin)

class VisualDefectAdmin(TranslationAdmin):
    pass

admin.site.register(VisualDefect, VisualDefectAdmin)