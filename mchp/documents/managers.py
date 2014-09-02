from django.db import models

import documents.models

from collections import namedtuple

class DocumentManager(models.Manager):
    def recent_events(self, course):
        if hasattr(course, 'pk'):
            pk = course.pk
        else:
            pk = course['pk']
        docs = documents.models.Document.objects.filter(
            course=pk
        ).select_related('upload')[:3]
        Activity = namedtuple('Activity', ['type', 'title', 'time', 'user'])
        events = []
        for doc in docs:
            events.append(Activity('document', doc, doc.create_date, doc.upload.owner))
        return events
