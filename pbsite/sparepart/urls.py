from django.conf.urls import url
from .views import SparePartDetail

urlpatterns = [
    url(r'detail/(?P<pk>.+)$', SparePartDetail.as_view(), name='spare_part_detail_url')
]