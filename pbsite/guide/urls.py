from django.conf.urls import url
from .views import GuideFormViev

urlpatterns = [
    url(r'create$', GuideFormViev.as_view(), name='guide_create_form'),
]