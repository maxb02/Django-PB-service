from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import BatteryIssue
from sncheck.validators import serial_number_length_validator, serial_number_validator


class BatteryIssueForm(forms.ModelForm):
    device_serial_number = forms.CharField(validators=[serial_number_length_validator, serial_number_validator])

    class Meta:
        model = BatteryIssue
        fields = ('device_serial_number', 'purchase_date', 'received_date', 'is_presale', 'battery_serial_number',
                  'battery_model', 'battery_batch', 'battery_production_date', 'battery_photo', 'general_view_photo')

        widgets = {
            'purchase_date': forms.DateInput(format=('%d/%m/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'received_date': forms.DateInput(format=('%d/%m/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'battery_production_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                              'type': 'week'}),
            'is_presale': forms.CheckboxInput(attrs={'id': 'is_presale'})
        }

        labels = {
            'general_view_photo': _(
                'Photo of general view of the device (with visible serial number on the back cover)'),
            'battery_photo': _('Photo of the battery label')
        }
