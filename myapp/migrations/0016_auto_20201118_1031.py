# Generated by Django 3.1.2 on 2020-11-18 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20201118_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(default='7404502132', max_length=10),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.CharField(default='5661527005', max_length=10),
        ),
    ]
