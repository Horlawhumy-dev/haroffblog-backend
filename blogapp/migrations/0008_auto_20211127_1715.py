# Generated by Django 3.2.9 on 2021-11-27 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20211127_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 27, 17, 15, 38, 416898)),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 27, 17, 15, 38, 416898)),
        ),
    ]
