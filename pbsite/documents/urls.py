from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^documents/request$', views.requestform, name='requestform'),
    url(r'^documents/showall', views.showall, name='showall'),
    url(r'^documents/act/(?P<id>.+)/$', views.act, name='act'),
    ]