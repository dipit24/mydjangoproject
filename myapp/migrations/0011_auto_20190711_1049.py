# Generated by Django 2.2.2 on 2019-07-11 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20190711_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='c_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 10, 49, 7, 117104)),
        ),
    ]
