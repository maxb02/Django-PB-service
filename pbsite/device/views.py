from django.views.generic import View
from django.shortcuts import get_object_or_404, render
from .models import Device



class DeviceDetail(View):
    def get(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        if request.user.is_staff:
            guides = device.guide_set.order_by('title').all()
        else:
            guides = device.guide_set.filter(group__in=request.user.groups.all()).order_by('-published_date')

        spare_parts = device.spare_parts.all()
        return render(request, 'device/device.html', {
            'device': device,
            'guides': guides,
            'spare_parts': spare_parts
        })
