from django import forms
from django.forms import modelform_factory
from .models import BatteryIssue


class BatteryIssueForm(forms.ModelForm):

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
