from haystack import indexes
from schedule.models import Course

class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    dept = indexes.CharField(model_attr='dept')
    course_number = indexes.CharField(model_attr='course_number')
    professor = indexes.CharField(model_attr='professor')
    domain = indexes.CharField(model_attr='domain')

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
