# Generated by Django 2.2rc1 on 2019-03-26 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 15, 30, 41, 568317, tzinfo=utc)),
        ),
    ]
