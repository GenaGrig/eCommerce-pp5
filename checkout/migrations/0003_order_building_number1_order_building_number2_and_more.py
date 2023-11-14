# Generated by Django 4.2.6 on 2023-11-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_order_street_address2'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='building_number1',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='order',
            name='building_number2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.CharField(default='', max_length=80),
        ),
    ]