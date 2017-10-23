from technicalguides.models import Device

def devices_menu(request):
    return {'devices': Device.objects.order_by('name')}