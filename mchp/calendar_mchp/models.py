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
    section = models.ForeignKey('schedule.section', related_name="calendar_sections")

    create_date = models.DateTimeField(auto_now_add=True)

    objects = ClassCalendarManager()

    class Meta:
        unique_together = (('owner', 'section'))

    def save(self, *args, **kwargs):
        if not self.pk: # object is new
            course = self.section.course
            self.title = course.dept + " " + str(course.course_number) + " Calendar"

        super(ClassCalendar, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

class CalendarEvent(models.Model):
    calendar = models.ForeignKey(ClassCalendar)

    title = models.CharField(max_length=30)
    all_day = models.BooleanField()
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    url = models.URLField(blank=True)
    
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
