from django.db import models
from django.utils import timezone
from . import utils
from calendar_mchp.models import CalendarEvent, Subscription, ClassCalendar
from notification.api import add_notification
import datetime
from schedule.models import Enrollment
import pytz

class Roster(models.Model):
    """ Roster.

    Attributes
    ----------
    course : django.db.models.ForeignKey
       A course to which this roster is attached.
    roster_html : django.db.models.TextField
        The roster HTML to parse.
    created : django.db.models.DateTimeField
        When was this roster first created?
    updated : django.db.models.DateTimeField
        When was this roster last updated?
    created_by : django.db.models.ForeignKey
        Who submitted this roster?
    status : django.db.models.CharField, optional
        What is the status of this roster?

    """
    PENDING = 'p'
    APPROVED = 'a'
    REJECTED = 'r'
    IMPORTED = 'i'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (IMPORTED, 'Imported'),
    )

    course = models.ForeignKey('schedule.Course')
    roster_html = models.TextField('roster HTML')
    instructor_emails = models.TextField('instructor emails')
    tz = 

    created = models.DateTimeField('first created', auto_now_add=True)
    updated = models.DateTimeField('last updated', auto_now=True)
    created_by = models.ForeignKey('user_profile.Student')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default=PENDING)

    def approve(self):
        """ Create users based on roster data.
        """
        if (self.status == self.APPROVED):
            pass

        primary_calendar = self.course.calendar_courses.get(primary=True)
        # print ('primary = ' + primary_calendar)
        for event in self.events.all():
            d = event.date
            start = datetime.datetime(d.year, d.month, d.day)
            end = datetime.datetime(d.year, d.month, d.day, 23, 55, 55)
            start = pytz.utc.localize(start)
            end = pytz.utc.localize(end)

            params = {
                    'calendar': primary_calendar,
                    'title': event.title,
                    'start': start,
                    'end': end
            }
            CalendarEvent.objects.create(**params)
            event.approved = True
            event.save()

        syllabus = self.syllabus.all()[0]
        syllabus.approved = True
        syllabus.course = self.course
        syllabus.save()


        for student in self.students.all():
            email = student.email
            if email:
                user = utils.get_or_create_user(email, student.first_name, student.last_name)
                school = self.course.domain
                user_student = utils.get_or_create_student(school, user)

                self.course.enroll_by_roster(user_student, self)

            student.approved = True
            student.save()

        for instructor in self.instructors.all():
            instructor.approved = True
            instructor.save()

        self.status = self.APPROVED
        self.save()

        add_notification(
            self.created_by.user,
            'Your class set for {}, is approved and published!'.format(self.course)
        )

    def reject(self):
        """ Create users based on roster data.
        """
        if (self.status == self.REJECTED):
            pass

        if (self.status == self.APPROVED):
            # remove existing events etc

            primary_calendar = self.course.calendar_courses.get(primary=True)
            # print ('primary = ' + primary_calendar)
            for event in self.events.all():
                params = {
                        'calendar': primary_calendar,
                        'title': event.title
                }
                events = CalendarEvent.objects.get(**params)
                for event in events:
                    event.approved = False
                    event.save()

            syllabus = self.syllabus.all()[0]
            syllabus.approved = False
            syllabus.course = None
            syllabus.save()


            for student in self.students.all():
                enroll = Enrollment.objects.filter(
                student=student,
                created_by_roster=self
                )

                if enroll.exists():
                    enroll.delete()

                    # Unsubscribing from all calendars
                    subscriptions = Subscription.objects.filter(student=self.student, calendar__course=self.course)
                    subscriptions.delete()

                    # Removing student calendars (events will cascade delete too)
                    calendars = ClassCalendar.objects.filter(owner=self.student, course=self.course)
                    calendars.delete()

                student.approved = False
                student.save()

            for instructor in self.instructors.all():
                instructor.approved = False
                instructor.save()


        self.status = self.REJECTED
        self.save()

        add_notification(
            self.created_by.user,
            'Your class set for {} has been rejected'.format(self.course)
        )

    def save(self, *args, **kwargs):
        from rosters.signals import roster_uploaded
        signal = False
        if not self.pk:
            signal = True
        super(Roster, self).save(*args, **kwargs)
        if signal:
            roster_uploaded.send(sender=self.__class__, roster=self)

    def __str__(self):
        return "{} :: {}".format(
            self.created_by,
            self.course)
    class Meta:
        verbose_name = 'Class Set'
        verbose_name_plural = 'Class Sets'


class RosterEventEntry(models.Model):
    """ Roster event entry.

    Parameters
    ----------
    roster : django.db.models.ForeignKey
        A roster associated with this entry.

    """
    title = models.CharField(max_length=30)
    date = models.DateField()
    roster = models.ForeignKey(Roster, related_name='events')

    class Meta:
        verbose_name = 'roster event entry'
        verbose_name_plural = 'roster event entries'


class RosterEntry(models.Model):
    """ Abstract base class for a roster entry.

    Parameters
    ----------
    first_name : django.db.models.CharField, optional
        A first name for the entry.
    last_name : django.db.models.CharField, optional
        A last name for the entry.
    email : django.db.models.CharField
        An email address for the entry.
    profile : django.db.models.ForeignKey, optional
        An optional user profile associated with this entry.

    """
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    profile = models.ForeignKey('user_profile.Student', blank=True, null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def clean(self):
        user = utils.get_user(self.email)
        if user:
            self.user = user

    def __str__(self):
        return '{}, {} ({})'.format(self.last_name, self.first_name,
                                    self.email)


class RosterStudentEntry(RosterEntry):
    """ Roster student entry.

    Parameters
    ----------
    roster : django.db.models.ForeignKey
        A roster associated with this entry.

    """
    roster = models.ForeignKey(Roster, related_name='students')

    class Meta:
        verbose_name = 'roster student entry'
        verbose_name_plural = 'roster student entries'


class RosterInstructorEntry(RosterEntry):
    """ Roster instructor entry.

    Parameters
    ----------
    roster : django.db.models.ForeignKey
        A roster associated with this entry.

    """
    roster = models.ForeignKey(Roster, related_name='instructors')

    class Meta:
        verbose_name = 'roster instructor entry'
        verbose_name_plural = 'roster instructor entries'