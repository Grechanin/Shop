from django import forms


class CheckoutContactForm(forms.Form):
    client_name = forms.CharField(required=True, max_length=100)
    phone = forms.IntegerField(required=True)