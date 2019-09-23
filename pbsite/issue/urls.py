from django.conf.urls import url
from .views import BattaryIssueCreate

urlpatterns = [
    url(r'^battery/create$', BattaryIssueCreate.as_view(), name='battery_issue_create_url'),
    ]