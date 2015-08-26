# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutemark_app', '0003_auto_20150819_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTable',
            fields=[
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('count_sources', models.IntegerField()),
                ('course_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'course_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LearningStreamTable',
            fields=[
                ('stream_id', models.IntegerField(serialize=False, primary_key=True)),
                ('count_sources', models.IntegerField()),
                ('stream_name', models.TextField()),
            ],
            options={
                'db_table': 'learning_stream_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SourceTable',
            fields=[
                ('source_id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.TextField()),
                ('marks', models.IntegerField()),
                ('marked_by', models.TextField()),
                ('weblink', models.TextField()),
                ('type', models.TextField()),
                ('fee', models.TextField()),
            ],
            options={
                'db_table': 'source_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StreamCourseGraphAdjacentNodeIds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_id', models.IntegerField()),
                ('next_node_id', models.IntegerField()),
            ],
            options={
                'db_table': 'stream_course_graph_adjacent_node_ids',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StreamCourseGraphsNodeTable',
            fields=[
                ('node_id', models.IntegerField(serialize=False, primary_key=True)),
                ('stream_or_course', models.TextField()),
                ('stream_id_or_course_id', models.IntegerField()),
            ],
            options={
                'db_table': 'stream_course_graphs_node_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaggingBetweenCourseAndTutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_id', models.IntegerField()),
                ('tutorial_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tagging_between_course_and_tutorial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TutorialTable',
            fields=[
                ('name', models.TextField()),
                ('count_sources', models.IntegerField()),
                ('tutorial_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'tutorial_table',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='source',
            name='marked_by',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
    ]
