from django.test import TestCase
from openpyxl.compat import tempfile

from device.models import Device
from models import SparePart, Category, Manufacturer, Supplier
from django.core.files.uploadedfile import SimpleUploadedFile


# class SparePartDeviceCategoryListTest:
#
#     @classmethod
#     def setUpTestData(cls):
#
#         def _create_image(self):
#             from PIL import Image
#             with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
#                 image = Image.new('RGB', (200, 200), 'white')
#                 image.save(f, 'PNG')
#
#             return open(f.name, mode='rb')
#
#         Device.objects.create(
#             name='632 | Touch HD 3',
#             model_number='632',
#             serial_number_prefix='G',
#             image =
#
#         )

