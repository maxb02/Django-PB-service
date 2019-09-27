from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from .forms import BatteryIssueForm
from .models import BatteryIssue





class BatteryIssueCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'issue.add_batteryissue'
    raise_exception = True
    model = BatteryIssue
    form_class = BatteryIssueForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BatteryIssueCreate, self).form_valid(form)


class BatteryIssueDetail(LoginRequiredMixin, DetailView):
    model = BatteryIssue


class BatteryIssueList(LoginRequiredMixin, ListView):
    permission_denied_message = 'issue.view_battery_issue_list'
    raise_exception = True
    model = BatteryIssue


