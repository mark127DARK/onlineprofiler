# Generated by Django 4.0.5 on 2022-06-14 06:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_comment_created_on_alter_user_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 6, 8, 42, 814772, tzinfo=utc)),
        ),
    ]
