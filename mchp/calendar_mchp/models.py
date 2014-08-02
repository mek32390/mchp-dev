from django.db import models
from django.core.urlresolvers import reverse
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

    create_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    objects = ClassCalendarManager()

    class Meta:
        unique_together = (('owner', 'course'))

    def save(self, *args, **kwargs):
        # object is new and doesn't have a title
        if not self.pk and not self.title: 
            self.title = str(self.course.dept) + " " + str(self.course.course_number) + " Calendar"

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

from schedule.utils import WEEK_DAYS
class CourseDay(models.Model):
    calendar = models.ForeignKey(ClassCalendar, related_name='calendar_course_days')
    event = models.ForeignKey(CalendarEvent, related_name='course_events')

    week_day_list = list(zip(range(10), WEEK_DAYS))
    day = models.PositiveSmallIntegerField(max_length=10, choices=week_day_list)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ("calendar", "day", "start_time", "end_time")

    def save(self, *args, **kwargs):
        if not self.pk: 
            self.event.title = self.calendar.course.dept + " " + str(self.calendar.course.course_number)
            self.event.url = reverse('course', kwargs={'number': self.calendar.course.pk})
            self.event.save()
        super(CourseDay, self).save(*args, **kwargs)

    
    def __str__(self):
        return "{} from {} to {}".format(WEEK_DAYS[self.day], self.start_time, self.end_time)
