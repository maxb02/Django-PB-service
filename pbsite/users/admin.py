from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User



ADDITIONAL_USER_FIELDS = (
    ('Service Center', {'fields': ('service_center',)}),
)

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'get_full_name', 'service_center', 'email', 'is_active', 'is_staff')

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

admin.site.register(User, CustomUserAdmin)