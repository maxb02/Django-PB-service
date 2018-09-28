from django.forms import ModelForm
from .models import Act

class ActRequestForm(ModelForm):
    class Meta:
        model = Act
        # fields = [serial_number, received_date, purchase_date, is_presale, document_type,
        #           client_name, seller_name, document_photo, screen_photo, defect_photo]
        fields = '__all__'