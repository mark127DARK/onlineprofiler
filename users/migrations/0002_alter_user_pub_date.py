# Generated by Django 4.0.5 on 2022-06-13 09:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 9, 19, 14, 286418, tzinfo=utc)),
        ),
    ]
