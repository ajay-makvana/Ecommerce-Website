# Generated by Django 3.1.7 on 2021-03-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210318_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
