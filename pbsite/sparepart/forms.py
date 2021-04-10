from django import forms

class CartAddSparePartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )