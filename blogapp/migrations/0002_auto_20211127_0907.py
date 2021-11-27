# Generated by Django 3.2.9 on 2021-11-27 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 27, 9, 7, 2, 885719)),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 27, 9, 7, 2, 885719)),
        ),
    ]