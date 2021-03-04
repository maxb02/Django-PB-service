from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Country
from .models import PhoneNumber
from .models import Email
from .models import Link


@admin.register(PhoneNumber)
class PhoneNumberAdmin(VersionAdmin):
    list_display = ('number', 'country',)
    list_filter = ('country',)


@admin.register(Country)
class CountryAdmin(VersionAdmin):
    list_display = ('name',)


@admin.register(Email)
class EmailAdmin(VersionAdmin):
    list_display = ('name', 'email')


@admin.register(Link)
class LinkAdmin(VersionAdmin):
    list_display = ('name', 'url')
