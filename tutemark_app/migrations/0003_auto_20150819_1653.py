# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutemark_app', '0002_auto_20150817_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='text_or_video',
            field=models.CharField(max_length=100, choices=[(b'TEXT', b'VIDEO')]),
        ),
    ]
