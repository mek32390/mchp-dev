from django.db import models
from . import utils


class Roster:
    """ Roster.

    Attributes
    ----------
    course : django.db.models.ForeignKey
       A course to which this roster is attached.
    html : django.db.models.TextField
        The roster HTML to parse.
    when : django.db.models.DateTimeField
        When was this roster submitted?
    created_by : django.db.models.ForeignKey
        Who submitted this roster?

    """
    course = models.ForeignKey('schedule.Course')
    html = models.TextField()
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
        items = utils.parse_roster(self.html)
        for item in items:
            email, fname, lname = item['email'], item['fname'], item['lname']
            user = utils.ensure_user_exists(email, fname=fname, lname=lname)
            student = utils.ensure_student_exists(self.course.domain, user)
            enrollment = utils.ensure_enrollment_exists(self.course, student)
            enrollments.append(enrollment)
        return len(enrollments)
