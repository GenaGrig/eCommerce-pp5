from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    '''Form for user profile'''
    class Meta:
        model = UserProfile
        
        # exclude = ('user',)  # exclude user field from form
        fields = ('default_first_name', 'default_last_name', 
                  'default_email_address', 
                  'default_phone_number', 'default_street_address1', 
                  'default_building_number1', 
                  'default_street_address2', 'default_building_number2', 
                  'default_city', 'default_postal_code', 'default_country')
        
    def __init__(self, *args, **kwargs):
        '''Add placeholders and classes, remove auto-generated labels
        and set autofocus on first field'''
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_email_address': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_building_number1': 'Building Number 1',
            'default_street_address2': 'Street Address 2',
            'default_building_number2': 'Building Number 2',
            'default_city': 'City',
            'default_postal_code': 'Postal Code',
        }
        
        # autofocus on first field
        self.fields['default_first_name'].widget.attrs['autofocus'] = True
        
        # add placeholders and classes to form fields
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


# class AlternativeUserProfileForm(forms.ModelForm):
#     '''Form for alternative user profile'''
#     class Meta:
#         model = UserProfile
#         exclude = ('user',)  # exclude user field from form
#         # fields = ('default_phone_number', 'default_street_address1', 'default_building_number1', 'default_street_address2', 'default_building_number2', 'default_city', 'default_postal_code', 'default_country')
#         # fields = '__all__'
        
#     def __init__(self, *args, **kwargs):
#         '''Add placeholders and classes, remove auto-generated labels
#         and set autofocus on first field'''
#         super().__init__(*args, **kwargs)
#         placeholders = {
#             'alternative_phone_number': 'Phone Number',
#             'alternative_street_address1': 'Street Address 1',
#             'alternative_building_number1': 'Building Number 1',
#             'alternative_street_address2': 'Street Address 2',
#             'alternative_building_number2': 'Building Number 2',
#             'alternative_city': 'City',
#             'alternative_postal_code': 'Postal Code',
#         }
        
#         # autofocus on first field
#         self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        
#         # add placeholders and classes to form fields
#         for field in self.fields:
#             if field != 'default_country':
#                 if self.fields[field].required:
#                     placeholder = f'{placeholders[field]} *'
#                 else:
#                     placeholder = placeholders[field]
#                 self.fields[field].widget.attrs['placeholder'] = placeholder
                
#             self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
#             self.fields[field].label = False

