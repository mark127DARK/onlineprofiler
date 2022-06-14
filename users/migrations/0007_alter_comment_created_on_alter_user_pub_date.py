# Generated by Django 4.0.5 on 2022-06-14 06:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default='date commented'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 6, 2, 17, 29198, tzinfo=utc)),
        ),
    ]