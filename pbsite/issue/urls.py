from django.conf.urls import url
from .views import BatteryIssueCreate, BatteryIssueDetail, BatteryIssueList, DisplayLineIssueCreate, \
    DisplayLineIssueDetail, DisplayLineIssueList

urlpatterns = [
    url(r'^battery/create$', BatteryIssueCreate.as_view(), name='battery_issue_create_url'),
    url(r'battery/detail/(?P<pk>.+)$', BatteryIssueDetail.as_view(), name='battery_issue_detail_url'),
    url(r'battery/list', BatteryIssueList.as_view(), name='battery_issue_list_url'),
    url(r'display-line/create$', DisplayLineIssueCreate.as_view(), name='display_line_issue_create_url'),
    url(r'display-line/detail/(?P<pk>.+)$', DisplayLineIssueDetail.as_view(), name='display_line_issue_detail_url'),
    url(r'display-line/list', DisplayLineIssueList.as_view(), name='display_line_issue_list_url'),

]
