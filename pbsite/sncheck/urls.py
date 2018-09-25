from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sncheck$', views.serialcheck, name='sncheck'),
    url(r'^snchecklist$', views.snchecklist, name='snchecklist'),

    ]

