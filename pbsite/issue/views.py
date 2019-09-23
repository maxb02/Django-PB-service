from django.shortcuts import render
from django.contrib import messages
from django.forms import formset_factory

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .forms import BatteryIssueForm
from .models import BatteryIssue



class BattaryIssueCreate(LoginRequiredMixin, View):

    def get(self, request):
        form = BatteryIssueForm
        return render(request, 'issue/battery_issue_create.html', {
            'form': form,

        })
