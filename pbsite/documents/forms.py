from django.forms import ModelForm
from django import forms
from .models import Act


class ActRequestForm(ModelForm):
    class Meta:
        model = Act
        fields = ('serial_number', 'client_name', 'protocol_number', 'received_date', 'purchase_date', 'is_presale',
                  'customers_claim', 'identified_malfunction', 'document_type', 'conclusion',
                  'accessories', 'visual_defect', 'comment_of_engineer', 'warranty_card_photo', 'receipt_photo',
                  'screen_photo', 'defect_photo',  )
        widgets = {
            'received_date': forms.DateInput(format=('%d/%m/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'purchase_date': forms.DateInput(format=('%d/%m/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'accessories' : forms.CheckboxSelectMultiple(),
            'visual_defect' : forms.CheckboxSelectMultiple()
        }

class ActComentForm(ModelForm):
    class Meta:
        model = Act
        fields = ('comment_of_manager',)