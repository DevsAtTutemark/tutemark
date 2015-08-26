import datetime
from haystack import indexes
from tutemark_app.models import Source

class SourceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    '''title = indexes.CharField(model_attr='title')
    weblink = indexes.CharField(model_attr='weblink')
    text_or_video = indexes.CharField(model_attr='text_or_video')
    fee = indexes.CharField(model_attr='fee')
    marked_by = indexes.CharField(model_attr='marked_by')
    marks = indexes.CharField(model_attr='marks')
    marked_date = indexes.DateTimeField(model_attr='marked_date')'''
    
    def get_model(self):
        return Source
    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated"""
        return self.get_model().objects.all()