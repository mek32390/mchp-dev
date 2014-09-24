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
        ).order_by('-create_date')[:3]
        Activity = namedtuple('Activity', ['type', 'title', 'time', 'user'])
        events = []
        for doc in docs:
            # upload = documents.models.Upload.objects.filter(
            #     document=doc
            # )
            # if upload.exists():
            #     owner = upload[0].owner
            # else:
            owner = None
            events.append(Activity('document', doc, doc.create_date, owner))
        return events
