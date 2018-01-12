from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Country
from .models import PhoneNumber
from .models import Email
from .models import Link


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'country',)
    list_filter = ('country',)

@admin.register(PhoneNumber)
class YourModelAdmin(VersionAdmin, PhoneNumberAdmin):
    pass

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Country)
class YourModelAdmin(VersionAdmin, CountryAdmin):
    pass

class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(Email)
class YourModelAdmin(VersionAdmin, EmailAdmin):
    pass

class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

@admin.register(Link)
class YourModelAdmin(VersionAdmin, LinkAdmin):
    pass

