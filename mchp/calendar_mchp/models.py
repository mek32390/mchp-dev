from django.db import models
from django.utils import timezone

from datetime import timedelta

from calendar_mchp.exceptions import TimeOrderError, CalendarExpiredError

class ClassCalendarManager(models.Manager):
    def default(self, student):
        calendar, created = ClassCalendar.objects.get_or_create(
            owner=student,
            title='default',
        )
        return calendar

class ClassCalendar(models.Model):
    owner = models.ForeignKey('user_profile.student', related_name="calendars")
    subscribers = models.ManyToManyField('user_profile.student', through='Subscription')

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=2000, blank=True)
    course = models.ForeignKey('schedule.course', related_name="calendar_courses")

    private = models.BooleanField(default=True)
    price = models.PositiveIntegerField(default=0)

    create_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    expire_date = models.DateTimeField()

    color = models.CharField(max_length=7, blank=True, default="#FFFFFF")

    objects = ClassCalendarManager()

    class Meta:
        unique_together = (('owner', 'course'))

    def save(self, *args, **kwargs):
        # object is new
        if not self.pk:
            # object is new and doesn't have a title
            if not self.title: 
                self.title = str(self.course.dept) + " " + str(self.course.course_number)
            # give this calendar a max lifetime
            self.expire_date = timezone.now() + timedelta(days=183)

        # don't let end date go past six months from calendar creation
        if self.end_date > self.expire_date:
            self.end_date = self.expire_date

        if(self.end_date > timezone.now()):
            super().save()
        else:
            raise TimeOrderError("Start date must come before end date")
        super(ClassCalendar, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    student = models.ForeignKey('user_profile.Student', related_name='subscribers')
    calendar = models.ForeignKey(ClassCalendar)

    price = models.PositiveIntegerField()
    payment_date = models.DateTimeField()
    subscribe_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # object is new
        if not self.pk:
            # set first payment date
            self.payment_date = self.subscribe_date + timedelta(days=30)
        super(Subscription, self).save(*args, **kwargs)

    def __str__(self):
        return "subscribed to {} on {}".format(self.calendar.title, self.subscribe_date)

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

    def save(self, *args, **kwargs):
        # don't let end date go past six months from calendar creation
        if self.end > self.calendar.end_date:
            raise CalendarExpiredError("You can not add events after a calendar's end date: {}".format(self.calendar.end_date.strftime('%B %d, %Y')))

        if(self.end > self.start):
            super().save()
        else:
            raise TimeOrderError("Start date must come before end date")
        super(CalendarEvent, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
