# Generated by Django 3.2.9 on 2021-11-27 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_auto_20211127_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 27, 20, 39, 46, 411561)),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 27, 20, 39, 46, 411561)),
        ),
    ]
