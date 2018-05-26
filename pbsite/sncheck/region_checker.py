from .models import AllowedDeviceRegion


def region_ceker(user, device_info):
    if (user.groups.filter(
            name='moderator').exists() or user.is_superuser or device_info == False or device_info == 'Erorr'):
        return True
    if not device_info or device_info == 'Erorr':
        for device_data in device_info:
            if AllowedDeviceRegion.objects.filter(
                    user_region=user.groups.all(), device_region=device_data['countryEng']).exists():
                return True
