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
    parsed_csv : django.db.models.TextField
        CSV parsed from the roster HTML.
    emails : django.db.models.TextField
        A whitespace-delimited list of email addresses to strip.
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
    parsed_csv = models.TextField('parsed CSV', blank=True)

    # [TODO] emails should eventually be inline with foreign key from other
    # model
    emails = models.TextField('filter emails', blank=True)

    when = models.DateTimeField('submitted', auto_now_add=True)
    created_by = models.ForeignKey('user_profile.Student')
    approved = models.DateTimeField(blank=True, null=True)
    imported = models.DateTimeField(blank=True, null=True)

    def _format_entry(self, d):
        """ Quick kludge to format a CSV entry like: "LAST, FIRST (EMAIL)"

        """
        return '{}, {} ({})'.format(d['last'], d['first'], d['email'])

    def preview(self):
        items = utils.csv_string_to_python(self.parsed_csv)
        return '\n'.join([self._format_entry(i) for i in items])

    def clean(self):
        """ Set parsed_csv on save.

        """
        self.parsed_csv = utils.roster_html_to_csv(self.roster_html)

    def import_roster(self):
        """ Ensure enrollments exist, based on an input roster.

        Returns
        -------
        out : int
            The number of enrollments created.

        """
        enrollments = []
        emails_to_filter = self.emails.split()
        items = utils.csv_string_to_python(self.parsed_csv)
        for item in items:
            email, fname, lname = item['email'], item['first'], item['last']
            if email not in emails_to_filter:
                user = utils.get_or_create_user(email,
                                                fname=fname,
                                                lname=lname)
                student = utils.get_or_create_student(self.course.domain, user)
                enrollment = utils.get_or_create_enrollment(self.course,
                                                            student)
                enrollments.append(enrollment)
        self.imported = timezone.now()
        self.save(update_fields=['imported'])
        return len(enrollments)
