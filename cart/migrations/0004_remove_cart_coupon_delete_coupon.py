# Generated by Django 4.2.6 on 2023-11-16 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='coupon',
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]