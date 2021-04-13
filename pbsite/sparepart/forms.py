from django import forms
from .models import Order


class CartAddSparePartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['destination',]