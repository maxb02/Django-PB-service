from device.models import Device


class DeviceModelFieldMixin:
    serial_number_field = 'serial_number'

    def get_queryset(self):
        devices = Device.objects.select_related('factory').values('model_number', 'code', 'factory__code').all()
        device_number_serial_number_prefix_dict = {
            '{}{}'.format(device['factory__code'], device['code']): device['model_number'] for device
            in devices}

        queryset = super().get_queryset()

        for obj in queryset:
            prefix = getattr(obj, self.serial_number_field)[:3]
            obj.model_number = device_number_serial_number_prefix_dict.get(prefix, None)

        return queryset
