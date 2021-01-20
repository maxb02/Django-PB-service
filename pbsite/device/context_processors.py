from device.models import Device


def devices_menu(request):
    return {'new_devices': Device.objects.values('name').order_by('name')}
