from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^devices/(?P<device_name>.+)/$', views.device, name='device'),
    url(r'^devices/(?P<device_name>.+)/(?P<title>.+)$', views.guide, name='guide'),
    ]
