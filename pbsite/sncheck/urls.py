from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sncheck/$', views.serialcheck, name='sncheck'),
    url(r'^sndetail', views.sndetail, name='sn_detail'),
    ]

