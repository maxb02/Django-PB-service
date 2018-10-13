from django.contrib import admin
from .models import Act, SerialNumberPrefix

@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    pass


@admin.register(SerialNumberPrefix)
class SerialNumberPrefixAdmin(admin.ModelAdmin):
    pass