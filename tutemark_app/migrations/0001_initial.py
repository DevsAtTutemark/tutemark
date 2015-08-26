# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('weblink', models.URLField()),
                ('marks', models.IntegerField()),
                ('text_or_video', models.BinaryField(verbose_name=1)),
                ('fee', models.TextField()),
                ('marked_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
