from django import forms
from .models import RefurbishmentDevice
from sncheck.validators import serial_number_length_validator, serial_number_validator
# from .validators import refurbishment_validator
from .models import Refurbishment
from django.core.exceptions import ValidationError


class RefurbishmentDeviceForm(forms.ModelForm):
    # old_serial_number = forms.CharField(validators=[serial_number_length_validator, serial_number_validator])
    # new_serial_number = forms.CharField(validators=[serial_number_length_validator, serial_number_validator])
    refurbishment = forms.ModelMultipleChoiceField(queryset=Refurbishment.objects.all())

    def clean_refurbishment(self):
        refurbishments_data = self.cleaned_data.get('refurbishment').values('id', 'prohibited_with')
        refurbishments = {refurbishment.get('id') for refurbishment in refurbishments_data}
        prohibited_refurbishments = {prohibited_refurbishment.get('prohibited_with') for prohibited_refurbishment in
                                     refurbishments_data}
        for refurbishment in refurbishments:
            if refurbishment in prohibited_refurbishments:
                raise ValidationError('These refurbishments are prohibited together')
        return self.cleaned_data['refurbishment']

    class Meta:
        model = RefurbishmentDevice
        fields = ['condition', 'old_serial_number', 'new_serial_number', 'refurbishment', 'defect', 'notes']
        widgets = {
            'old_serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'new_serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'refurbishment': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'defect': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        }
