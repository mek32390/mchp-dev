from django.conf import settings
from django.db import models
from django.utils import timezone

from calendar_mchp.exceptions import TimeOrderError, CalendarExpiredError, BringingUpThePastError
from calendar_mchp.signals import calendar_event_created, calendar_event_edited, subscription
from calendar_mchp.utils import generate_calendar_color
from documents.models import Document
from django.core.urlresolvers import reverse


class ClassCalendarManager(models.Manager):
    def default(self, student):
        calendar, created = ClassCalendar.objects.get_or_create(
            owner=student,
            title='default',
        )
        return calendar

class ClassCalendar(models.Model):
    owner = models.ForeignKey('user_profile.Student', related_name="calendars")
    subscribers = models.ManyToManyField('user_profile.Student', through='Subscription')

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=2000, blank=True)
    course = models.ForeignKey('schedule.Course', related_name="calendar_courses")

    private = models.BooleanField(default=True)

    # primary Course calendar - created automatically when creating the Course
    # new students are auto-subscribed to the primary calendar of the Course
    primary = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    expire_date = models.DateTimeField()

    color = models.CharField(max_length=7, blank=True)

    objects = ClassCalendarManager()

    class Meta:
        unique_together = (('owner', 'course'))

    def save(self, *args, **kwargs):
        # object is new
        if not self.pk:
            # object is new and doesn't have a title
            if not self.title: 
                self.title = str(self.course.dept) + " " + str(self.course.course_number)

            # TODO remove expire_date and migrate the database
            # give this calendar a max lifetime
            self.expire_date = timezone.now() + settings.MCHP_PRICING['calendar_expiration']

            if not self.color:
                calendars = ClassCalendar.objects.filter(owner=self.owner)
                self.color = generate_calendar_color(calendars)

        if(self.end_date > timezone.now()):
            super().save()
        else:
            raise TimeOrderError("Start date must come before end date")
        # always end on the last minute of the day 
        self.end_date = self.end_date.replace(hour=11, minute=59)

        super(ClassCalendar, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    student = models.ForeignKey('user_profile.Student')
    calendar = models.ForeignKey(ClassCalendar)

    subscribe_date = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # object is new
        if not self.pk:
            # not allowed to follow private calendars
            # this should raise an exception
            if self.calendar.private:
                return
            # set first payment date
            self.subscribe_date = timezone.now()
            subscription.send(sender=self.__class__, subscription=self)
        super(Subscription, self).save(*args, **kwargs)

    def __str__(self):
        return "subscribed to {} on {}".format(self.calendar.title, self.subscribe_date)


class CalendarEvent(models.Model):
    """

    Attributes
    ----------
    DEFAULT_NOTIFY_LEAD : int
        Default lead time for event notifications.
    notify_lead : django.db.models.PositiveIntegerField, optional
        A lead time, in minutes, for mailings before events.
        For example, 24 hours => 2880 minutes.
    title : django.db.models.CharField
        The name of the event.
    description : django.db.models.CharField
        A description of the event.
    documents : django.db.models.ManyToManyField, optional
        Documents to associate optionally with this event.

    """
    DEFAULT_NOTIFY_LEAD = 60 * 24 * 2  # 48 hours

    calendar = models.ForeignKey(ClassCalendar)

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    all_day = models.BooleanField(default=False)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    url = models.URLField(blank=True)

    is_recurring = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField()

    notify_lead = models.PositiveIntegerField(default=DEFAULT_NOTIFY_LEAD,
                                              blank=True)
    documents = models.ManyToManyField(Document,
                                       related_name='events',
                                       blank=True,
                                       null=True)

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.pk:
            # first time
            edit = False
        else:
            edit = True

        # don't let end date go past six months from calendar creation
        if self.end > self.calendar.end_date:
            end_date = timezone.localtime(
                self.calendar.end_date, 
                timezone.get_current_timezone()
            ).strftime('%B %d, %Y')
            raise CalendarExpiredError(
                "You can not add events after this calendar's end date: {}"\
                .format(end_date)
            )

        if self.start < timezone.now():
            raise BringingUpThePastError(
                "You can not change the past. Give it up, Gatsby."
            )

        if(self.end > self.start):
            super().save()
        else:
            raise TimeOrderError("Event start date must come before end date")
        self.last_edit = timezone.now()
        super(CalendarEvent, self).save(*args, **kwargs)

        if edit:
            calendar_event_edited.send(sender=self.__class__, event=self)
        else:
            calendar_event_created.send(sender=self.__class__, event=self)

    def __str__(self):
        return self.title
