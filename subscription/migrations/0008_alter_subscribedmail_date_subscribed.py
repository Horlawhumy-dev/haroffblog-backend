# Generated by Django 3.2.9 on 2021-12-15 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0007_alter_subscribedmail_date_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribedmail',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 22, 1, 23, 301102)),
        ),
    ]