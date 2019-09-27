from django.conf.urls import url
from .views import BatteryIssueCreate, BatteryIssueDetail, BatteryIssueList

urlpatterns = [
    url(r'^battery/create$', BatteryIssueCreate.as_view(), name='battery_issue_create_url'),
    url(r'battery/detail/(?P<pk>.+)$', BatteryIssueDetail.as_view(), name='battery_issue_detail_url'),
    url(r'battery/list', BatteryIssueList.as_view(), name='battery_issue_list_url'),


    ]