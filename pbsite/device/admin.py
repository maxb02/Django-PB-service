from django.contrib import admin
from django import forms
from .models import Device, SKU, Region, Color, Module, Project, Factory


class SKUInline(admin.TabularInline):
    model = SKU

class DeviceAdminForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = 'name', 'model_number', 'code', 'factory', 'image',



@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('model_number', 'name', 'serial_number_prefix')
    form = DeviceAdminForm
    inlines = [SKUInline,]


admin.site.register(SKU)
admin.site.register(Region)
admin.site.register(Color)
admin.site.register(Module)
admin.site.register(Project)
admin.site.register(Factory)
