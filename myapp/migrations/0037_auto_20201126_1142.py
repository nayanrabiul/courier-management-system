# Generated by Django 3.1.2 on 2020-11-26 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_product_delivery_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_date',
            new_name='delivery_date',
        ),
    ]
