from collections import defaultdict

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
from .models import SparePart, Category
from device.models import Device


class SparePartDetail(LoginRequiredMixin, DetailView):
    model = SparePart


class SparePartDeviceList(LoginRequiredMixin, View):
    def get(self, request, pk):
        device = get_object_or_404(Device.objects.prefetch_related('spare_parts__category'), pk=pk)
        categories = defaultdict(list)

        for spare_part in device.spare_parts.all():
            categories[spare_part.category.name].append(spare_part)

        return render(request, 'sparepart/sparepart_list.html', {
            'device': device,
            'categories': dict(categories),
        })
