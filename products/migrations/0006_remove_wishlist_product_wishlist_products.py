# Generated by Django 4.2.6 on 2023-10-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
