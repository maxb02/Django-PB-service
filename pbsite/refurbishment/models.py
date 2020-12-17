from django.conf import settings
from django.db import models
from django.urls import reverse
from device.models import Device
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def valid(prohibited_with):
    pass

class Refurbishment(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Refurbishment name'))
    prohibited_with = models.ManyToManyField('self', null=True, blank=True,validators=[valid,])

    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    #     if db_field.name == 'prohibited_with':
    #         # set the query set to whatever you like
    #         kwargs['queryset'] = request._obj.client.clienturls.all()
    #     return super(Refurbishment,
    #                  self).formfield_for_foreignkey(request, obj, **kwargs)

    def __str__(self):
        return self.name


class Defect(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Defect name'))

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Condition nmae'))

    def __str__(self):
        return self.name


class RefurbishmentDevice(models.Model):
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

    def get_model(self):
        return Device.objects.filter(serial_number_prefix=self.new_serial_number[:3]).first()

    get_model.short_description = _('Model')

    def get_was_returned(self):
        if self.was_returned:
            return _('Yes')
        else:
            return _('No')
