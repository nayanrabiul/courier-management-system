# Generated by Django 3.1.2 on 2020-11-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20201118_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(blank=True, default='3229445361', editable=False, max_length=10, unique=True),
        ),
    ]
