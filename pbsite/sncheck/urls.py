from django.conf.urls import url
from .views import SerialNumberCheck, SerialNumberInfo, snchecklist

urlpatterns = [
    url(r'^sncheck$', SerialNumberCheck.as_view(), name='serial_number_check_url'),
    url(r'^sninfo/(?P<serial_number>.+)/$', SerialNumberInfo.as_view(), name='serial_number_info_url'),
    url(r'^snchecklist$', snchecklist, name='snchecklist'),

]
