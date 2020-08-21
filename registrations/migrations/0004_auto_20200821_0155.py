# Generated by Django 3.1 on 2020-08-20 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0003_auto_20200816_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='close',
            field=models.BooleanField(choices=[(1, 'yes'), (0, 'no')], default=1),
        ),
        migrations.AddField(
            model_name='person',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='interaction',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='lay',
            field=models.BooleanField(choices=[(1, 'yes'), (0, 'no')], default=1),
        ),
        migrations.AddField(
            model_name='person',
            name='looks',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='nationality',
            field=models.CharField(default='NA', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='person_age',
            field=models.IntegerField(blank=True, choices=[(16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45)], null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='reply',
            field=models.BooleanField(choices=[(1, 'yes'), (0, 'no')], default=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='duration',
            field=models.CharField(choices=[('Short', 'Short'), ('Medium', 'Medium'), ('Long', 'Long')], default='NA', max_length=30),
        ),
    ]
