from django import forms
from .models import BilligAddress

class BillingForm(forms.ModelForm):
    class Meta:
        model = BilligAddress
        fields = ['address','zipcode', 'city', 'country']