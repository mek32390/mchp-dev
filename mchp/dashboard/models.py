from django.db import models
from django.utils import timezone

from dashboard.utils import DASH_EVENT_LIST
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

    student = models.ForeignKey('user_profile.Student', related_name='target')
    followers = models.ManyToManyField('user_profile.Student', related_name='followers')

    document = models.ForeignKey('documents.Document', blank=True, null=True)
    calendar = models.ForeignKey('calendar_mchp.ClassCalendar', blank=True, null=True)
    event = models.ForeignKey('calendar_mchp.CalendarEvent', blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)

class RSSType(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=30)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class RSSLink(models.Model):
    rss_type = models.ForeignKey(RSSType)

    name = models.CharField(max_length=30)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
        return "{}: {}::{}".format(self.rss_type.name, self.name, self.url)

class RSSSetting(models.Model):
    student = models.ForeignKey('user_profile.Student')
    rss_type = models.ForeignKey(RSSType)

    objects = managers.RSSSettingManager()

    class Meta:
        unique_together = (('student', 'rss_type'))

    def __str__(self):
        return "setting {} for {}".format(self.rss_type, self.student.user.username)
