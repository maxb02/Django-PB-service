from django.contrib import admin
from .models import Supplier, Manufacturer, SparePart, Category


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_select_related = ('device', 'supplier', 'manufacturer', 'category')
    list_display = ('name', 'device', 'category', 'sku', 'purchase_price', 'supplier', 'manufacturer')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
