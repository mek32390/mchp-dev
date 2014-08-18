from django.db import models

from dashboard.utils import RSS_LIST
from dashboard import managers

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
