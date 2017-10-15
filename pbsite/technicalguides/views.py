from django.shortcuts import render, get_object_or_404
from .models import Device, News, Guide
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    news = News.objects.order_by('-published_date')
    guides = (Guide.objects.order_by('-updated_date'))
    number_of_guid= 3
    if len(guides) >=number_of_guid:
        last_update_guides = guides[:number_of_guid]
    else:
        last_update_guides = guides
    return render(request, 'technicalguides/index.html', {'news': news,
                                                          'last_update_guides': last_update_guides
                                                          })

@login_required
def device(request, device_name):
    device = get_object_or_404(Device, name=device_name)
    guides = device.guide_set.all()

    return render(request, 'technicalguides/device.html', {'device': device, 'guides': guides})

@login_required
def guide(request, device_name, title):
    guide = get_object_or_404(Device, name = device_name).guide_set.get(title= title)
    return render(request, 'technicalguides/guide.html', {'guide': guide, 'device_name': device_name})

@login_required
def serialcheck(request):
    return render(request, 'technicalguides/serialcheck.html')

def contacts(request):
    return render(request, 'technicalguides/contacts.html')

