# Generated by Django 3.1.2 on 2020-11-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20201118_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(default='1502947279929568', max_length=10),
        ),
    ]
