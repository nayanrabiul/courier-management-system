# Generated by Django 3.1.2 on 2020-11-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_auto_20201119_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
