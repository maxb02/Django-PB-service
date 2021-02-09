from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^documents/request$', views.ActCreate.as_view(), name='document_request_url'),
    url(r'^documents/list', views.ActList.as_view(), name='document_list_url'),
    url(r'^documents/detail/(?P<number>.+)$', views.ActDetail.as_view(), name='document_detail_url'),
    url(r'^documents/accept_or_reject/(?P<number>.+)$', views.ActAcceptOrReject.as_view(),
        name='document_accept_or_reject_url'),
    url(r'^documents/compensation_status/(?P<pk>.+)$', views.ActCompensationStatusUpdate.as_view(),
        name='compensation_status_url'),
    url(r'^documents/pdf/(?P<number>.+)$', views.ActGeneratePDF.as_view(), name='document_generate_pdf_url'),
]
