from django.db import models

import dashboard.models
from dashboard.utils import RSS_LIST

class RSSSettingManager(models.Manager):
    def toggle_setting(self, student, rss):
        setting, created = dashboard.models.RSSSetting.objects.get_or_create(
            student=student,
            rss_type=rss,
        )
        if not created:
            setting.delete()
        return created

    def restore_default_settings(self, student):
        dashboard.models.RSSSetting.objects.filter(
            student=student
        ).delete()
        for rss in RSS_LIST:
            dashboard.models.RSSSetting(student=student, rss_type=rss[0]).save()

        return dashboard.models.RSSSetting.objects.filter(
            student=student
        )
