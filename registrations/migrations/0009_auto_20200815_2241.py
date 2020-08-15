# Generated by Django 3.1 on 2020-08-15 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0008_auto_20200815_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='current_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 15, 22, 41, 45, 966017)),
        ),
    ]