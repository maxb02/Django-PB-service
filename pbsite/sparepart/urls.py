from django.conf.urls import url
from .views import SparePartDetail, SparePartDeviceList, cart_detail, cart_add, cart_remove

urlpatterns = [
    url(r'detail/(?P<pk>.+)$', SparePartDetail.as_view(), name='spare_part_detail_url'),
    url(r'list/(?P<pk>.+)$', SparePartDeviceList.as_view(), name='spare_part_device_list_url'),

    url(r'cart/$', cart_detail, name='cart_detail'),
    url(r'cart/add(?P<spare_part_id>.+)$', cart_add, name='cart_add'),
    url(r'cart/remove(?P<spare_part_id>.+)$', cart_remove, name='cart_remove'),
]
