from django.conf.urls import url
from .views import SparePartDetail, SparePartDeviceList

urlpatterns = [
    url(r'detail/(?P<pk>.+)$', SparePartDetail.as_view(), name='spare_part_detail_url'),
    url(r'list/(?P<pk>.+)$', SparePartDeviceList.as_view(), name='spare_part_device_list_url'),
]
