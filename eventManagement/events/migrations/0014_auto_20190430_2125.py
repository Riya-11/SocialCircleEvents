# Generated by Django 2.1.7 on 2019-04-30 21:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_merge_20190430_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 30, 21, 25, 24, 113324, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event_archive',
            name='ev_start_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 30, 21, 25, 24, 114732, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 30, 21, 25, 24, 116378, tzinfo=utc)),
        ),
    ]
