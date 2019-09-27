from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import datetime

def upload_path_handler(self, filename):
    return "issue/battery/{device_serial_number}/{date}/{file}".format(device_serial_number=self.device_serial_number,
                                                                       date=datetime.datetime.now().strftime(
                                                                           "%Y.%m.%d"),
                                                                       file=filename)


class BatteryIssue(models.Model):
    device_serial_number = models.CharField(max_length=20, verbose_name=_('Device Serial Number'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', verbose_name=_('User Name'))
    filling_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Fill Date'))
    purchase_date = models.DateField(verbose_name=_('Purchase Date'))
    received_date = models.DateField(verbose_name=_('Received Date'))
    is_presale = models.BooleanField(verbose_name=_('Presale'))
    battery_serial_number = models.CharField(max_length=20, verbose_name=_('Battery Serial Number'))
    battery_model = models.CharField(max_length=20, verbose_name=_('Battery Model'))
    battery_batch = models.CharField(max_length=20, verbose_name=_('Battery Batch'))
    battery_production_date = models.DateField(verbose_name=_('Battery Production Date'))
    battery_photo = models.ImageField(upload_to=upload_path_handler, verbose_name=_('Battery photo'))
    general_view_photo = models.ImageField(upload_to=upload_path_handler, verbose_name=_('General view photo'))


