# Generated by Django 3.2.9 on 2021-11-27 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contactmessage_sent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='sent_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 20, 30, 55, 310666)),
        ),
    ]