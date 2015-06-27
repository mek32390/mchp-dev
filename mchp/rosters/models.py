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
    emails : django.db.models.TextField
        A whitespace-delimited list of email addresses to strip.
    when : django.db.models.DateTimeField
        When was this roster submitted?
    created_by : django.db.models.ForeignKey
        Who submitted this roster?
    reviewed : django.db.models.DateTimeField, optional
        When was this roster reviewed?
    imported : django.db.models.DateTimeField, optional
        When was this roster imported?

    """
    course = models.ForeignKey('schedule.Course')
    roster_html = models.TextField('roster HTML')

    # [TODO] emails should eventually be inline with foreign key from other
    # model
    emails = models.TextField('filter emails', blank=True)

    when = models.DateTimeField('submitted', auto_now_add=True)
    created_by = models.ForeignKey('user_profile.Student')
    reviewed = models.DateTimeField(blank=True, null=True)
    imported = models.DateTimeField(blank=True, null=True)

    def import_roster(self):
        """ Ensure enrollments exist, based on an input roster.

        Returns
        -------
        out : int
            The number of enrollments created.

        """
        enrollments = []
        emails_to_filter = self.emails.split()
        for entry in self.entries:
            if entry.email not in emails_to_filter:
                user = utils.get_or_create_user(entry.email,
                                                fname=entry.first_name,
                                                lname=entry.last_name)
                student = utils.get_or_create_student(self.course.domain, user)
                enrollment = utils.get_or_create_enrollment(self.course,
                                                            student)
                enrollments.append(enrollment)
        self.imported = timezone.now()
        self.save(update_fields=['imported'])
        return len(enrollments)


class RosterEntry(models.Model):
    """ Roster import entry.

    """
    roster = models.ForeignKey(Roster, related_name='entries')
    first_name = models.CharField(max_length=30)  # 30 is max length for users
    last_name = models.CharField(max_length=30)   # 30 is max length for users
    email = models.EmailField(max_length=255)
    profile = models.ForeignKey('user_profile.Student', blank=True, null=True)

    def clean(self):
        user = utils.get_user(self.email)
        if user:
            self.user = user

    def __str__(self):
        return '{}, {} ({})'.format(self.last_name, self.first_name,
                                    self.email)
