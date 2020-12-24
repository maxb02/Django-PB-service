from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, UpdateView
from .forms import BatteryIssueForm, DisplayLineIssueForm, ClockIssueForm
from .models import BatteryIssue, DisplayLineIssue, ClockIssue


class BatteryIssueCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = BatteryIssue
    form_class = BatteryIssueForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BatteryIssueCreate, self).form_valid(form)


class BatteryIssueDetail(LoginRequiredMixin, DetailView):
    model = BatteryIssue


class BatteryIssueList(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'issue.view_battery_issue_list'
    raise_exception = True
    queryset = BatteryIssue.objects.all().select_related('user', 'user__service_center')


class DisplayLineIssueCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = DisplayLineIssue
    form_class = DisplayLineIssueForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DisplayLineIssueCreate, self).form_valid(form)


class DisplayLineIssueDetail(LoginRequiredMixin, DetailView):
    model = DisplayLineIssue


class DisplayLineIssueList(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'issue.view_display_line_issue_list'
    raise_exception = True
    queryset = DisplayLineIssue.objects.all().select_related('user', 'user__service_center')


class ClockIssueCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = ClockIssue
    queryset = ClockIssue.objects.all().select_related('user', 'user__service_center__name')
    form_class = ClockIssueForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClockIssueCreate, self).form_valid(form)


class ClockIssueList(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'issue.view_clock_issue_list'
    raise_exception = True
    queryset = ClockIssue.objects.all().select_related('user', 'user__service_center')
    model = ClockIssue


class ClockIssueDetail(LoginRequiredMixin, DetailView):
    model = ClockIssue
    queryset = ClockIssue.objects.all().select_related('user', 'user__service_center')
