from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Act, SerialNumberPrefix, VisualDefect, ScopeOfSupply


@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    list_display = ('number',
                    'get_region', 'get_service', 'get_model', 'serial_number', 'document_type', 'status',
                    'filling_date',
                    'received_date', 'purchase_date')
    search_fields = 'number', 'serial_number'


@admin.register(SerialNumberPrefix)
class SerialNumberPrefixAdmin(admin.ModelAdmin):
    pass


class ScopeOfSupplyAdmin(TranslationAdmin):
    pass


admin.site.register(ScopeOfSupply, ScopeOfSupplyAdmin)


class VisualDefectAdmin(TranslationAdmin):
    pass


admin.site.register(VisualDefect, VisualDefectAdmin)
