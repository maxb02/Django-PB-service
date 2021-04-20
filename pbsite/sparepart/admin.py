from django.contrib import admin
from django.utils.html import format_html

from .models import Supplier, Manufacturer, SparePart, Category, Order, OrderSupplier, OrderItem
from .order import get_supplier_order_file_response


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_select_related = ('supplier', 'manufacturer', 'category')
    list_display = ('sku', 'name', 'get_device', 'category', 'purchase_price', 'supplier', 'manufacturer')
    list_filter = 'supplier', 'device', 'category'

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


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = 'spare_part',
    # # fields = ['quantity', 'price']


@admin.register(OrderSupplier)
class OrderSupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_created_date', 'get_service_center', 'supplier', 'status', 'update_date',
                    'invoice_number',
                    'post_service', 'track_number', 'estimated_delivery_date', 'get_file']
    readonly_fields = ['get_service_center', 'supplier', 'update_date', 'delivered_date', 'get_destination', 'id']
    inlines = [OrderItemInline]
    fields = ['id', 'get_service_center',  'supplier', 'status', 'invoice_number', 'post_service',
              'track_number', 'estimated_delivery_date', ]

    def get_service_center(self, obj):
        return obj.order.created_by.service_center.company_name

    get_service_center.admin_order_field = 'service center'
    get_service_center.short_description = 'Service Center'

    def get_destination(self, obj):
        return obj.order.destination

    get_destination.admin_order_field = 'destination'
    get_destination.short_description = 'Destination'

    def get_created_date(self, obj):
        return obj.order.created_date

    get_created_date.admin_order_field = 'created date'
    get_created_date.short_description = 'Created date'

    def get_file(self, obj):
        return format_html('<a href={}><span class="ui-icon  ui-icon-document"></span></a>'.format(obj.get_excel_file_url()))
    get_file.admin_order_field = 'get_exl_file'
    get_file.short_description = 'Get Excel File '
