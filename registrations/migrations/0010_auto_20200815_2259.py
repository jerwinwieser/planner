# Generated by Django 3.1 on 2020-08-15 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0009_auto_20200815_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='current_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 15, 22, 59, 2, 876376)),
        ),
    ]
