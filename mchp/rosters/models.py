from django.db import models
from django.utils import timezone
from . import utils


class Roster(models.Model):
    """ Roster.

    Attributes
    ----------
    course : django.db.models.ForeignKey
       A course to which this roster is attached.
    roster_html : django.db.models.TextField
        The roster HTML to parse.
    emails : django.db.models.TextField, optional
        A whitespace-delimited set of e-mail addresses for staff
        who should be excluded from study guide campaign outreach.
        [TODO] This should not be required as a part of the model,
               just a part of the form.
    when : django.db.models.DateTimeField
        When was this roster submitted?
    created_by : django.db.models.ForeignKey
        Who submitted this roster?
    approved : django.db.models.DateTimeField, optional
        When was this roster approved?
    imported : django.db.models.DateTimeField, optional
        When was this roster imported?

    """
    course = models.ForeignKey('schedule.Course')
    roster_html = models.TextField('roster HTML')

    emails = models.TextField('filter emails', blank=True)

    when = models.DateTimeField('submitted', auto_now_add=True)
    created_by = models.ForeignKey('user_profile.Student')
    approved = models.DateTimeField(blank=True, null=True)
    imported = models.DateTimeField(blank=True, null=True)

    def import_roster(self):
        """ Create users based on roster data.

        Returns
        -------
        out : int
            The number of enrollments created.

        """
        enrollments = []
        emails_to_filter = [entry.email for entry in self.instructors]
        students = [student for student in self.students
                    if student.email not in emails_to_filter]
        for entry in students:
            user = utils.get_or_create_user(entry.email,
                                            fname=entry.first_name,
                                            lname=entry.last_name)
            student = utils.get_or_create_student(self.course.domain, user)
            enrollment = utils.get_or_create_enrollment(self.course, student)
            enrollments.append(enrollment)
        self.imported = timezone.now()
        self.save(update_fields=['imported'])
        return len(enrollments)


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
