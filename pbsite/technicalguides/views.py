from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Device


@login_required
def device(request, device_name):
    device = get_object_or_404(Device, name=device_name)
    if request.user.is_staff:
        guides = device.guide_set.order_by('title').all()
    else:
        guides = device.guide_set.filter(group__in=request.user.groups.all()).order_by('-published_date')

    return render(request, 'technicalguides/device.html', {'device': device, 'guides': guides,})

@login_required
def guide(request, device_name, title):
    guide = get_object_or_404(Device, name = device_name).guide_set.get(title= title)
    return render(request, 'technicalguides/guide.html', {'guide': guide, 'device_name': device_name})


