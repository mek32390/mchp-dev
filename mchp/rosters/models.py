from django.db import models
from . import utils


class Roster(models.Model):
    """ Roster.

    Attributes
    ----------
    course : django.db.models.ForeignKey
       A course to which this roster is attached.
    source : django.db.models.TextField
        The roster HTML to parse.
    emails : django.db.models.TextField
        A whitespace-delimited list of email addresses to strip.
    when : django.db.models.DateTimeField
        When was this roster submitted?
    created_by : django.db.models.ForeignKey
        Who submitted this roster?

    """
    course = models.ForeignKey('schedule.Course')
    source = models.TextField('source code')
    # [TODO] emails should eventually be inline with foreign key
    emails = models.TextField('filter emails', blank=True)
    when = models.DateTimeField('submitted', auto_now_add=True)
    created_by = models.ForeignKey('user_profile.Student')

    def approve(self):
        """ Ensure enrollments exist, based on an input roster.

        Returns
        -------
        out : int
            The number of enrollments created.

        """
        enrollments = []
        emails_to_filter = self.emails.split()
        items = utils.parse_roster(self.html)
        for item in items:
            email, fname, lname = item['email'], item['fname'], item['lname']
            if email not in emails_to_filter:
                user = utils.get_or_create_user(email,
                                                fname=fname,
                                                lname=lname)
                student = utils.get_or_create_student(self.course.domain, user)
                enrollment = utils.get_or_create_enrollment(self.course,
                                                            student)
                enrollments.append(enrollment)
        return len(enrollments)
