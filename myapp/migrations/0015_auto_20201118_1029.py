# Generated by Django 3.1.2 on 2020-11-18 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20201118_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(blank=True, default='4224230934', editable=False, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.CharField(max_length=10),
        ),
    ]
