# Generated by Django 3.2.9 on 2022-01-28 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0011_alter_subscribedmail_date_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribedmail',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 19, 56, 50, 244240)),
        ),
    ]
