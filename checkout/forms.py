from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    '''Create a form for the user to fill in their details'''
    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'email_address', 'phone_number',
            'street_address1', 'street_address2', 'city', 'postal_code',
            'country',
        )

    def __init__(self, *args, **kwargs):
        '''Add placeholders and classes, remove auto-generated labels
        and set autofocus on first field'''
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'city': 'City',
            'postal_code': 'Postal Code',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
