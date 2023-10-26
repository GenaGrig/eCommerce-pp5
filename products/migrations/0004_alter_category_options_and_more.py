# Generated by Django 4.2.6 on 2023-10-24 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_product_brand_product_product_color_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category_name',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]