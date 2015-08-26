from django.db import models
from django.contrib.auth.models import User

'''class Source(models.Model):
    TEXT_OR_VIDEO = (
        ('TEXT', 'VIDEO'),
    )
    marked_by = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    weblink = models.URLField()
    marks = models.IntegerField()
    text_or_video = models.CharField(max_length=100, choices=TEXT_OR_VIDEO)
    fee = models.CharField(max_length=80)
    marked_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title'''

class CourseTable(models.Model):
    name = models.TextField()
    description = models.TextField()
    count_sources = models.IntegerField()
    course_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'course_table'

class LearningStreamTable(models.Model):
    stream_id = models.IntegerField(primary_key=True)
    count_sources = models.IntegerField()
    stream_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'learning_stream_table'


class SourceTable(models.Model):
    source_id = models.IntegerField(primary_key=True)
    title = models.TextField()
    marks = models.IntegerField()
    marked_by = models.TextField()
    weblink = models.TextField()
    type = models.TextField()  # This field type is a guess.
    fee = models.TextField()

    class Meta:
        managed = False
        db_table = 'source_table'


class StreamCourseGraphAdjacentNodeIds(models.Model):
    node_id = models.IntegerField()
    next_node_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stream_course_graph_adjacent_node_ids'


class StreamCourseGraphsNodeTable(models.Model):
    node_id = models.IntegerField(primary_key=True)
    stream_or_course = models.TextField()  # This field type is a guess.
    stream_id_or_course_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stream_course_graphs_node_table'


class TaggingBetweenCourseAndTutorial(models.Model):
    subject_id = models.IntegerField()
    tutorial_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tagging_between_course_and_tutorial'


'''class TutemarkAppSource(models.Model):
    title = models.CharField(max_length=100)
    weblink = models.CharField(max_length=200)
    marks = models.IntegerField()
    text_or_video = models.CharField(max_length=100)
    fee = models.CharField(max_length=80)
    marked_by = models.ForeignKey(AuthUser)
    marked_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tutemark_app_source'
'''

class TutorialTable(models.Model):
    name = models.TextField()
    count_sources = models.IntegerField()
    tutorial_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tutorial_table'    