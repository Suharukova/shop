from django import forms

from orders import models
from orders.models import PaymentType


class NewOrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        exclude = ['state']

