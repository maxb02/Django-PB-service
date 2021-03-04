from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import admin
from .models import Device, FileBrowser
from .models import Guide
from reversion.admin import VersionAdmin

@admin.register(Guide)
class GuideAdmin(VersionAdmin):
    list_display = ('title', 'device', 'updated_date')
    list_filter = ('device', 'updated_date', )

@admin.register(Device)
class DeviceAdmin(VersionAdmin):
    pass


@admin.register(FileBrowser)
class FileBrowserAdmin(admin.ModelAdmin):
    actions = []

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):
        opts = self.model._meta
        info = opts.app_label, (opts.model_name if hasattr(opts, 'model_name') else opts.module_name)
        return [
            url('^$', self.admin_site.admin_view(self.filebrowser_view), name='{0}_{1}_changelist'.format(*info)),
        ]

    def filebrowser_view(self, request):
        return HttpResponseRedirect(reverse('filebrowser:fb_browse'))

