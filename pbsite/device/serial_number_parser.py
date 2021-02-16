from collections import namedtuple
from urllib import response

from django.http import HttpResponseNotFound, Http404

from device.exceptions import SKUDoesNotExist
from device.models import Device


def parse_serial_number(serial_number):
    ParsedSerialNumber = namedtuple('ParsedSerialNumber', [
        'factory_code',
        'model_code',
        'module_code',
        'region_code',
        'project_code',
        'color_code',
    ])
    parsed_serial_number = ParsedSerialNumber(
        factory_code=serial_number[0:2],
        model_code=serial_number[2:3],
        module_code=serial_number[12:14],
        region_code=serial_number[14:15],
        project_code=serial_number[15:18],
        color_code=serial_number[18:19]
    )
    return parsed_serial_number


def get_model_sku_color(serial_number):
    parsed_serial_number = parse_serial_number(serial_number)
    try:
        info = Device.objects.filter(
            factory__code=parsed_serial_number.factory_code,
            code=parsed_serial_number.model_code,
            skus__module__code=parsed_serial_number.module_code,
            skus__region__code=parsed_serial_number.region_code,
            skus__project__code=parsed_serial_number.project_code,
            skus__color__code=parsed_serial_number.color_code, ).values('name', 'skus__name',
                                                                        'skus__color__name', ).first()
    except Device.DoesNotExist:
        raise SKUDoesNotExist(serial_number)

    return info
