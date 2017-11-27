from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),

    url(r'^serialcheck/', views.serialcheck, name='serialchek'),
    url(r'^devices/(?P<device_name>.+)/$', views.device, name='device'),
    url(r'^devices/(?P<device_name>.+)/(?P<title>.+)$', views.guide, name='guide'),
    ]
