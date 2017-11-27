from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contacts/', views.contacts, name='contacts'),
    ]