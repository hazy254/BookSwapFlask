# Generated by Django 2.2.2 on 2019-06-19 11:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20190619_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='listed_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 11, 7, 18, 469884, tzinfo=utc)),
        ),
    ]
