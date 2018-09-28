from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import url, static
from django.conf import settings
from django.conf.urls import include



urlpatterns = [
    url(r'', include('main.urls')),
    url(r'', include('technicalguides.urls')),
    url(r'', include('contacts.urls')),
    url(r'', include('sncheck.urls')),
    url(r'', include('documents.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

