# Generated by Django 2.2.2 on 2019-07-28 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassBasedViews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='dateandtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 28, 7, 16, 9, 327173)),
        ),
    ]
