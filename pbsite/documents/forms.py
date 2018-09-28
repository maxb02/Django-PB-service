from django.forms import ModelForm
from django import forms
from .models import Act


class ActRequestForm(ModelForm):
    class Meta:
        model = Act
        fields = ('serial_number', 'received_date', 'purchase_date', 'is_presale', 'customers_claim', 'identified_malfunction', 'document_type',
                  'client_name', 'seller_name', 'warranty_card_photo', 'receipt_photo', 'screen_photo', 'defect_photo')
        widgets = {
            'received_date': forms.DateInput(format=('%d/%m/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'purchase_date': forms.DateInput(format=('%d/%m/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }

