# Generated by Django 4.2.6 on 2023-11-18 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_coupon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GiftCoupon',
            new_name='Coupon',
        ),
    ]
