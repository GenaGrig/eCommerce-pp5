# Generated by Django 4.2.6 on 2023-10-29 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='code',
            new_name='coupon_code',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='active',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='discount_percentage',
        ),
        migrations.AddField(
            model_name='coupon',
            name='discount_price',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='coupon',
            name='isExpired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coupon',
            name='minimum_price',
            field=models.IntegerField(default=0),
        ),
    ]
