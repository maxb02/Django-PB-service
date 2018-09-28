from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^documents/request$', views.requestform, name='requestform'),
    ]
