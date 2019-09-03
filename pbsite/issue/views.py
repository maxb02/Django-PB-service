from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .forms import BatteryImageForm, BatteryIssue, BatteryImageFormSet
from .models import BatteryImage, BatteryIssue


class BattaryIssueCreate(LoginRequiredMixin, View):
    def get_login_url(self, request):
        form = BatteryIssue
        formset = BatteryImageFormSet(queryset=BatteryImage.objects.none())
        return render(request, 'issue/battery_issue_create.html')
