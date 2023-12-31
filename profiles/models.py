from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    '''A user profile model for maintaining default delivery information
    and order history'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_first_name = models.CharField(max_length=40, null=True, blank=True)
    default_last_name = models.CharField(max_length=40, null=True, blank=True)
    default_email_address = (models.EmailField(max_length=254, null=True,
                                               blank=True))
    default_phone_number = (models.CharField(max_length=20, null=True,
                                             blank=True))
    default_street_address1 = (models.CharField(max_length=80, null=True,
                                                blank=True))
    default_building_number1 = (models.CharField(max_length=80, null=True,
                                                 blank=True))
    default_street_address2 = (models.CharField(max_length=80, null=True,
                                                blank=True))
    default_building_number2 = (models.CharField(max_length=80, null=True,
                                                 blank=True))
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_postal_code = (models.CharField(max_length=20, null=True,
                                            blank=True))
    default_country = (CountryField(blank_label='Country', null=False,
                                    blank=False))

    def __str__(self):
        return f"Profile for {self.user.username}" if self.user else "Profile"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    '''Create or update the user profile'''
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
