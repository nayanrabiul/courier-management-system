# Generated by Django 3.1.2 on 2020-11-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_auto_20201126_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_date',
            field=models.DateField(),
        ),
    ]
