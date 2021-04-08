from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
from .models import SparePart, Category
from device.models import Device


class SparePartDetail(LoginRequiredMixin, DetailView):
    model = SparePart


class SparePartDeviceList(LoginRequiredMixin, View):
    def get(self, request, pk):
        device = get_object_or_404(Device.objects.prefetch_related('spare_parts'), pk=pk)
        categorys = Category.objects.filter(spare_parts__device__pk=device.pk)
        return render(request, 'sparepart/sparepart_list.html', {
            'device': device,
            'categorys': categorys,
        })
