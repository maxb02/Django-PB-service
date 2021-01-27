from django.conf import settings
from django.db import models
from django.urls import reverse
from device.models import Device
from django.utils.translation import gettext_lazy as _

class Refurbishment(models.Model):
    """Contain a type of refurbishment (a type of repair)"""
    name = models.CharField(max_length=255, verbose_name=_('Refurbishment name'))
    prohibited_with = models.ManyToManyField('self', null=True, blank=True)

    def __str__(self):
        return self.name


class Defect(models.Model):
    """Contain a defect of device before refurbishment"""
    name = models.CharField(max_length=255, verbose_name=_('Defect name'))

    def __str__(self):
        return self.name


LABEL_DATE_FIELD_NAME_CHOICE = (
    ('prd', 'Production date'),
    ('ref', 'Refurbish date')
)


class Condition(models.Model):
    """Mark the kind of device after refurbishment"""
    name = models.CharField(max_length=255, verbose_name=_('Condition name'))
    sku_suffix = models.CharField(max_length=5, verbose_name=_('Suffix for base SKU'), null=True, blank=True)
    label_date_field_name = models.CharField(choices=LABEL_DATE_FIELD_NAME_CHOICE, max_length=3)

    def __str__(self):
        return self.name


class RefurbishmentDevice(models.Model):
    """Refurbished device item"""
    old_serial_number = models.CharField(max_length=20, unique=True, verbose_name=_('Old Serial Number'))
    new_serial_number = models.CharField(max_length=20, unique=True, verbose_name=_('New Serial Number'))
    refurbishment = models.ManyToManyField(Refurbishment, verbose_name=_('Refurbishment'), validators=())
    defect = models.ManyToManyField(Defect, verbose_name=_('Defect'))
    condition = models.ForeignKey(Condition, verbose_name=_('Refurbishment Device Condition'))
    notes = models.TextField(max_length=255, blank=True, null=True, verbose_name=_('Notes'))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of creation'))
    update_date = models.DateTimeField(auto_now=True, verbose_name=_('Date of update'))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='refurbishment_device_created',
                                   verbose_name=_('Created By User'))
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                                   related_name='refurbishment_device_updated', verbose_name=_('Updated By User'))
    was_returned = models.BooleanField(default=False, verbose_name=_('Device was returned'))

    class Meta:
        permissions = (('view_refurbishment_device_list', 'User can view a list of Refurbishment Devices'),
                       ('can_mark_refurbishment_device_as_returned', 'User Can Mark Refurbishment Devices As Returned'))

    def __str__(self):
        return '{} | {}'.format(self.new_serial_number, self.created_by)

    def get_absolute_url(self):
        return reverse('refurbishment_device_detail_url', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('refurbishment_device_update_url', kwargs={'pk': self.pk})

    def get_label_url(self):
        return reverse('refurbishment_device_label_url', kwargs={'pk': self.pk})

    def get_was_returned(self):
        """A humanized status which show was the device returned or not"""
        if self.was_returned:
            return _('Yes')
        else:
            return _('No')



