from django import forms


class ItemSortForm(forms.Form):
    order_by = forms.ChoiceField(choices=[
        ('name', 'name [A-Z]'),
        ('-name', 'name [Z-A]'),
        ('price', 'price'),
        ('-price', 'price (desc)'),
        ('count', 'count'),
    ], label='Order', required=False)


class ItemFilterForm(forms.Form):
    name__contains = forms.CharField(max_length=200, required=False, label='Name')
    price__gt = forms.DecimalField(decimal_places=2, max_digits=15, required=False, label='Price >')
    price__lt = forms.DecimalField(decimal_places=2, max_digits=15, required=False, label='Price <')
