from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
import datetime


def upload_path_handler(self, filename):
    return "document/{serial_number}/{date}/{file}".format(serial_number=self.serial_number,
                                                           date=datetime.datetime.now().strftime("%Y.%m.%d"),
                                                           file=filename)


class ScopeOfSupply(models.Model):
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item


class VisualDefect(models.Model):
    defect = models.CharField(max_length=50)

    def __str__(self):
        return self.defect


class SerialNumberPrefix(models.Model):
    model = models.CharField(max_length=50, verbose_name='Device name')
    prefix = models.CharField(max_length=3, verbose_name='Serial Number Prefix')

    def __str__(self):
        return self.model


class Act(models.Model):
    DOCUMENT_TYPE_CHOICES = (
        ('warranty_rejection', _('Statement of manufacturer warranty rejection')),
        ('technical_inspection', _('Statement of manufacturer technical inspection')),
        ('defect_acceptance', _('Statement of  manufacturer defect acceptance')),
        ('discount_voucher_50', 'Statement of  manufacturer defect acceptance and 50% discount voucher'),
        ('discount_voucher_20', 'Statement of  manufacturer defect acceptance and 20% discount voucher'),
    )
    STATUS_CHOICES = (
        ('in_process', _('In Process')),
        ('confirmed', _('Confirmed')),
        ('rejected', _('Rejected')),
    )

    COMPENSATION_STATUS_CHOICES = (
        ('nc_nr', 'NOT compensated/NOT returned'),
        ('nc_r', 'NOT compensated/Returned'),
        ('c_nr', 'Compensated/NOT returned'),
        ('c_n', 'Compensated/Returned'),
    )

    class Meta:
        ordering = ['-filling_date']
        permissions = (('accept_or_decline_acts', 'User can accept or decline acts'),)

    serial_number = models.CharField(max_length=20, verbose_name=_('Serial Number'), db_index=True)
    protocol_number = models.CharField(max_length=10, null=True, verbose_name=_('Protocol Number'))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='created_by',
                                   verbose_name=_('User Name'))
    accepted_or_declined_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                                                related_name='accepted_or_declined_by',
                                                verbose_name=_('Accepted or declined by'))
    filling_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Fill Date'))
    purchase_date = models.DateField(verbose_name=_('Purchase Date'))
    received_date = models.DateField(verbose_name=_('Received Date'))
    conclusion_date = models.DateTimeField(null=True, blank=True, verbose_name=_('Conclusion Date'))
    is_presale = models.BooleanField(verbose_name=_('Presale'))

    customers_claim = models.CharField(max_length=300, verbose_name=_('Customer Claim'))
    identified_malfunction = models.CharField(max_length=50, verbose_name=_('Identified Malfunction'))
    conclusion = models.TextField(max_length=240, null=True, verbose_name=_('Conclusion'))
    warranty_card_photo = models.ImageField(null=True, blank=True, upload_to=upload_path_handler,
                                            verbose_name=_('Photo of warranty card'))
    receipt_photo = models.ImageField(null=True, blank=True, upload_to=upload_path_handler,
                                      verbose_name=_('Photo of receipt'))
    screen_photo = models.ImageField(null=True, blank=True, upload_to=upload_path_handler,
                                     verbose_name=_('Photo of screen'))
    defect_photo = models.ImageField(null=True, blank=True, upload_to=upload_path_handler,
                                     verbose_name=_('Photo of defect'))

    client_name = models.CharField(max_length=50, verbose_name=_('Client Name'))
    document_type = models.CharField(max_length=100, verbose_name=_('Document type'), choices=DOCUMENT_TYPE_CHOICES)
    status = models.CharField(max_length=50, verbose_name=_('Satatus'), default='in_process', choices=STATUS_CHOICES)
    scope_of_supply = models.ManyToManyField('ScopeOfSupply', blank=True, verbose_name=_('Scope of Supply'))
    visual_defect = models.ManyToManyField('VisualDefect', blank=True, verbose_name=_('Visual (cosmetic) Defects:'))
    comment_of_engineer = models.TextField(max_length=500, null=True, blank=True,
                                           verbose_name=_('Comments (for PocketBook)'))
    comment_of_manager = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('Comment of Manager'))
    number = models.CharField(max_length=50, verbose_name=_('Document Number'), db_index=True, null=True, blank=True)
    compensation_status = models.CharField(max_length=5, choices=COMPENSATION_STATUS_CHOICES, default='nc_nr', null=True)

    def __str__(self):
        return self.serial_number

    def save(self, *args, **kwargs):
        """Custom save method add calculated 'number' field"""
        super().save(*args, **kwargs)
        if not self.number:
            self._calculate_number()
            super().save(update_fields=['number'])

    def get_absolute_url(self):
        return reverse('document_detail_url', kwargs={'number': self.number})

    def get_pdf_url(self):
        return reverse('document_generate_pdf_url', kwargs={'number': self.number})

    def _calculate_number(self):
        self.number = '{}{}{}{}'.format(self.serial_number[:5], self.id, self.created_by.id,
                                        self.created_by.service_center.id)
        return self.number
