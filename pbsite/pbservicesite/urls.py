from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import url, static
from django.conf import settings
from django.conf.urls import include



urlpatterns = [
    url(r'', include('technicalguides.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', admin.site.urls),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

