from django import forms
from django.forms import modelform_factory
from .models import BatteryIssue, BatteryImage


class BatteryIssueForm(forms.ModelForm):
    class Meta:
        model = BatteryIssue
        fields = ('device_serial_number', 'purchase_date', 'received_date', 'is_presale', 'battery_serial_number',
                  'battery_model', 'battery_batch', 'battery_production_date')


class BatteryImageForm(forms.ModelForm):
    class Meta:
        model = BatteryImage
        fields = ('image',)

BatteryImageFormSet = modelform_factory(BatteryImage, form=BatteryImageForm, extra=3)

