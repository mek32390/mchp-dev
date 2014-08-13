from django.db import models
from django.utils import timezone

from calendar_mchp.exceptions import TimeOrderError

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
                                         db_table='calendar_mchp_calendarsubscription')

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=2000, blank=True)
    course = models.ForeignKey('schedule.course', related_name="calendar_courses")

    private = models.BooleanField(default=True)
    price = models.PositiveIntegerField(default=0)

    create_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    color = models.CharField(max_length=7, blank=True, default="#FFFFFF")

    objects = ClassCalendarManager()

    class Meta:
        unique_together = (('owner', 'course'))

    def save(self, *args, **kwargs):
        # object is new and doesn't have a title
        if not self.pk and not self.title: 
            self.title = str(self.course.dept) + " " + str(self.course.course_number)

        if(self.end_date > timezone.now()):
            super().save()
        else:
            raise TimeOrderError("Start date must come before end date")
        super(ClassCalendar, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class CalendarEvent(models.Model):
    calendar = models.ForeignKey(ClassCalendar)

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    all_day = models.BooleanField(default=False)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    url = models.URLField(blank=True)

    is_recurring = models.BooleanField(default=False)
    
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
