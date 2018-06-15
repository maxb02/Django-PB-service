from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Device


@login_required
def device(request, device_name):
    device = get_object_or_404(Device, name=device_name)
    guides = device.guide_set.order_by('title').all()
    group_guides = device.guide_set.order_by('title').filter(group=request.user.groups.all())

    return render(request, 'technicalguides/device.html', {'device': device, 'guides': guides, 'group_guides': group_guides})

@login_required
def guide(request, device_name, title):
    guide = get_object_or_404(Device, name = device_name).guide_set.get(title= title)
    return render(request, 'technicalguides/guide.html', {'guide': guide, 'device_name': device_name})


