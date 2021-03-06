from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.urls import reverse
from device.models import Device


def upload_path_handler(self, filename):
    return "issue/battery/{device_serial_number}/{date}/{file}".format(device_serial_number=self.device_serial_number,
                                                                       date=datetime.now().strftime(
                                                                           "%Y.%m.%d"),
                                                                       file=filename)


class BatteryIssue(models.Model):
    device_serial_number = models.CharField(max_length=20, verbose_name=_('Device Serial Number'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='user', verbose_name=_('User Name'))
    filling_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Fill Date'))
    purchase_date = models.DateField(verbose_name=_('Purchase Date'), null=True)
    received_date = models.DateField(verbose_name=_('Received Date'))
    is_presale = models.BooleanField(verbose_name=_('Presale'), default=False)
    battery_serial_number = models.CharField(max_length=20, verbose_name=_('Battery Serial Number'))
    battery_model = models.CharField(max_length=20, verbose_name=_('Battery Model'))
    battery_batch = models.CharField(max_length=20, verbose_name=_('Battery Batch'))
    battery_production_date = models.CharField(max_length=8, verbose_name=_('Battery Production Date'))
    battery_photo = models.ImageField(upload_to=upload_path_handler, null=True, verbose_name=_('Battery photo'))
    general_view_photo = models.ImageField(upload_to=upload_path_handler, null=True,
                                           verbose_name=_('General view photo'))

    class Meta:
        permissions = (('view_battery_issue_list', 'User can view a list of objects'),)
        unique_together = ('device_serial_number', 'received_date')

    def get_absolute_url(self):
        return reverse('battery_issue_detail_url', kwargs={'pk': self.pk})

    def get_battery_production_date(self):
        return datetime.strptime('{}-{}'.format(self.battery_production_date, '0'), '%Y-W%U-%w')

    def get_model(self):
        return Device.objects.filter(serial_number_prefix=self.device_serial_number[:3]).first()

    get_model.short_description = _('Model')

    def __str__(self):
        return 'Battery Issue {}, {}'.format(self.id, self.device_serial_number)


def display_line_upload_path_handler(self, filename):
    return "issue/display-line/{device_serial_number}/{date}/{file}".format(
        device_serial_number=self.device_serial_number,
        date=datetime.now().strftime(
            "%Y.%m.%d"),
        file=filename)


class DisplayLineIssue(models.Model):
    device_serial_number = models.CharField(max_length=20, verbose_name=_('Device Serial Number'), unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='display_line_issues',
                             verbose_name=_('User Name'))
    filling_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Fill Date'))
    purchase_date = models.DateField(verbose_name=_('Purchase Date'), null=True)
    received_date = models.DateField(verbose_name=_('Received Date'))
    is_presale = models.BooleanField(verbose_name=_('Presale'), default=False)
    display_photo = models.ImageField(upload_to=display_line_upload_path_handler, verbose_name=_('Display photo'))
    display_label_photo = models.ImageField(upload_to=display_line_upload_path_handler,
                                            verbose_name=_('Display label photo'))
    warranty_card_photo = models.ImageField(null=True, blank=True, upload_to=display_line_upload_path_handler,
                                            verbose_name=_('Photo of warranty card'))
    receipt_photo = models.ImageField(null=True, blank=True, upload_to=display_line_upload_path_handler,
                                      verbose_name=_('Photo of receipt'))

    class Meta:
        permissions = (('view_display_line_issue_list', 'User can view a list of objects'),)

    def get_model(self):
        return Device.objects.filter(serial_number_prefix=self.device_serial_number[:3]).first()

    get_model.short_description = _('Model')

    def get_absolute_url(self):
        return reverse('display_line_issue_detail_url', kwargs={'pk': self.pk})


class ClockIssue(models.Model):
    device_serial_number = models.CharField(max_length=20, verbose_name=_('Device Serial Number'), unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='clock_line_issues',
                             verbose_name=_('User Name'))
    filling_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Fill Date'))
    purchase_date = models.DateField(verbose_name=_('Purchase Date'), null=True, blank=True,
                                     help_text='Fill purchase date if available')
    comments = models.TextField(null=True, blank=True, verbose_name=_('Comments'))

    class Meta:
        permissions = (('view_clock_issue_list', 'User can view a list of Clock Issues'),)

    def get_model(self):
        return Device.objects.filter(serial_number_prefix=self.device_serial_number[:3]).first()

    get_model.short_description = _('Model')

    def get_absolute_url(self):
        return reverse('clock_issue_detail_url', kwargs={'pk': self.pk})

