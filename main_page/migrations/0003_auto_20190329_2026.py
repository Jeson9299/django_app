# Generated by Django 2.2rc1 on 2019-03-29 14:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_auto_20190326_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='img1',
            field=models.ImageField(default='NULL', upload_to='dog_image/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 29, 14, 56, 4, 269967, tzinfo=utc)),
        ),
    ]
