from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^technicalgiude/detail/(?P<pk>.+)$', views.TechnicalGuideDetail.as_view(),
        name="technocalguide_by_pk_detail_url"),
    #оставлен для сохранения работоспособности старых ссылок на инструкции
    url(r'^devices/(?P<device_name>.+)/(?P<title>.+)$', views.guide, name='technocalguide_by_name_detail_url'),
]
