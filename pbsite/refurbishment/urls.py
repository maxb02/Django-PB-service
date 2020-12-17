from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'ref/create/', views.RefurbishmentDeviceCreate.as_view(), name='refurbishment_device_create_url'),
    url(r'ref/list/', views.RefurbishmentDeviceList.as_view(), name='refurbishment_device_list_url'),
    url(r'ref/detail/(?P<pk>.+)$', views.RefurbishmentDeviceDetail.as_view(), name='refurbishment_device_detail_url'),
    url(r'ref/update/(?P<pk>.+)$', views.RefurbishmentDeviceUpdate.as_view(), name='refurbishment_device_update_url'),
]
