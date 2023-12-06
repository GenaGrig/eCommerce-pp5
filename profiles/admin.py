from django.contrib import admin


from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    '''Admin view for the user profile'''
    list_display = (
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_building_number1',
        'default_street_address2',
        'default_building_number2',
        'default_city',
        'default_postal_code',
        'default_country',
    )

    ordering = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
