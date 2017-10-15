from technicalguides.models import Device

def devices_menu(request):
    return {'devices': Device.objects.all()}