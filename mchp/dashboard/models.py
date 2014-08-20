from django.db import models
from django.utils import timezone

from dashboard.utils import RSS_LIST, DASH_EVENT_LIST
from dashboard import managers

from jsonfield import JSONField

class Weather(models.Model):
    zipcode = models.CharField(max_length=11, unique=True)
    info = JSONField()
    fetch = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.fetch = timezone.now()
        super(Weather, self).save(*args, **kwargs)


class DashEvent(models.Model):
    type = models.PositiveSmallIntegerField(choices=DASH_EVENT_LIST)
    course = models.ForeignKey('schedule.Course')

    student = models.ForeignKey('user_profile.Student')
    document = models.ForeignKey('documents.Document', blank=True, null=True)
    calendar = models.ForeignKey('calendar_mchp.ClassCalendar', blank=True, null=True)
    event = models.ForeignKey('calendar_mchp.CalendarEvent', blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)

class RSSLink(models.Model):
    rss_type = models.PositiveSmallIntegerField(choices=RSS_LIST)

    name = models.CharField(max_length=30)
    url = models.URLField(blank=True)

    def __str__(self):
        return "{}: {}::{}".format(RSS_LIST[self.rss_type][1], self.name, self.url)

class RSSSetting(models.Model):
    student = models.ForeignKey('user_profile.Student')
    rss_type = models.PositiveSmallIntegerField(choices=RSS_LIST)

    objects = managers.RSSSettingManager()

    class Meta:
        unique_together = (('student', 'rss_type'))

    def __str__(self):
        return "setting {}. {}".format(self.rss_type, RSS_LIST[self.rss_type][1])
