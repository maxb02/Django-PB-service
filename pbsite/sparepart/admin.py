from django.contrib import admin
from .models import Supplier, Manufacturer, SparePart, Category


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):

    list_select_related = ('supplier', 'manufacturer', 'category')
    list_display = ('name', 'get_device', 'category', 'sku', 'purchase_price', 'supplier', 'manufacturer')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.prefetch_related('device')
        return qs

    def get_device(self, obj):
        return ', '.join([device.model_number for device in obj.device.all()])
    get_device.short_description = 'Devices'

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
