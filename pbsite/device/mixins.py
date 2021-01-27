from device.models import Device
from device.serial_number_parser import parse_serial_number


class DevicesListAddModelNumberFieldMixin:
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


class DeviceAddModelNumberFieldMixin:
    serial_number_field = 'serial_number'

    def get_object(self):
        obj = super().get_object()
        serial_number = getattr(obj, self.serial_number_field)
        parsed_serial_number = parse_serial_number(serial_number)
        try:
            device = Device.objects.values('model_number').get(code=parsed_serial_number.model_code,
                                                               factory__code=parsed_serial_number.factory_code)
            model_number = device.get('model_number')
        except Device.DoesNotExist:
            model_number = None

        obj.model_number = model_number
        return obj
