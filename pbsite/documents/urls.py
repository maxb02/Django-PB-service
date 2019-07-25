from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^documents/request$', views.DocumentRequest.as_view(), name='document_request_url'),
    url(r'^documents/list', views.document_list, name='document_list_url'),
    url(r'^documents/detail/(?P<number>.+)$', views.DocumentDetail.as_view(), name='document_detail_url'),
    url(r'^documents/pdf/(?P<number>.+)$', views.generate_pdf, name='document_generate_pdf_url'),
    ]