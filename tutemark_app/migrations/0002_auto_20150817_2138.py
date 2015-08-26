# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tutemark_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='marked_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 21, 38, 49, 70151, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='source',
            name='fee',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='source',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
