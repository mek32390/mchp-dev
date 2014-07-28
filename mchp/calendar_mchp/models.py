from django.db import models

class ClassCalendarManager(models.Manager):
    def default(self, student):
        calendar, created = ClassCalendar.objects.get_or_create(
            owner=student,
            title='default',
        )
        return calendar

class ClassCalendar(models.Model):
    owner = models.ForeignKey('user_profile.student', related_name="calendars")
    subscribers = models.ManyToManyField('user_profile.student',
                                         db_table='calendar_mchp_calendarsubscription', blank=True)

    title = models.CharField(max_length=150)
    section = models.ForeignKey('schedule.section', related_name="calendar_sections", 
                                blank=True, null=True)

    objects = ClassCalendarManager()

    class Meta:
        unique_together = ('owner', 'title')

    def __str__(self):
        return str(self.title)

class CalendarEvent(models.Model):
    calendar = models.ForeignKey(ClassCalendar)

    title = models.CharField(max_length=30)
    all_day = models.BooleanField()
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return str(self.title)
