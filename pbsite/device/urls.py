from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'detail/(?P<pk>.+)$', views.DeviceDetail.as_view(), name='device_detail_url'),
]