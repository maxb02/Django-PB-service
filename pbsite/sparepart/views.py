from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import SparePart

class SparePartDetail(LoginRequiredMixin, DetailView):
    model = SparePart
