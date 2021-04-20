from django.conf.urls import url
from .views import SparePartDetail, SparePartDeviceList, cart_detail, cart_add, cart_remove, OrderCreateView, \
    OrderSupplierListView, OrderCreatedView, OrderSupplierDetailView

urlpatterns = [
    url(r'sp/detail/(?P<pk>.+)$', SparePartDetail.as_view(), name='spare_part_detail_url'),
    url(r'sp/list/(?P<pk>.+)$', SparePartDeviceList.as_view(), name='spare_part_device_list_url'),

    url(r'cart/$', cart_detail, name='cart_detail'),
    url(r'cart/add(?P<spare_part_id>.+)$', cart_add, name='cart_add'),
    url(r'cart/remove(?P<spare_part_id>.+)$', cart_remove, name='cart_remove'),

    url(r'order/create/$', OrderCreateView.as_view(), name='order_create'),
    url(r'order/created/(?P<pk>.+)$', OrderCreatedView.as_view(), name='order_created'),
    url(r'order/detail/(?P<pk>.+)$', OrderSupplierDetailView.as_view(), name='order_detail'),
    url(r'order/list/$', OrderSupplierListView.as_view(), name='order_list'),
]
