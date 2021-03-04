from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import include
from filebrowser.sites import site

admin.site.site_header = "Pocketbook Service Portal Admin"
admin.site.site_title = "PB Service Admin Portal"
admin.site.index_title = "Welcome to Pocketbook Service Portall"

urlpatterns = [
    url(r'', include('main.urls')),
    url(r'', include('technicalguides.urls')),
    url(r'', include('contacts.urls')),
    url(r'', include('sncheck.urls')),
    url(r'', include('documents.urls')),
    url(r'^issue/', include('issue.urls')),
    url(r'device/', include('device.urls')),
    url(r'sparepart/', include('sparepart.urls')),
    url(r'refurbishment/', include('refurbishment.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),

                  ] + urlpatterns

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)