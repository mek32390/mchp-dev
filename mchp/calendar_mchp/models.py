from django.db import models

class ClassCalendar(models.Model):
    pass

class CalendarEvent(models.Model):
    title = models.CharField(max_length=30)
    allDay = models.BooleanField()
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
