from django import forms

from . import utils


class RosterUploadForm(forms.Form):
    roster = forms.CharField(widget=forms.Textarea)

    def parse_roster(self, course):
        """ Ensure enrollments exist, based on an input roster.

        Parameters
        ----------
        course : schedule.models.Course
            A course in which to enroll students.

        Returns
        -------
        out : int
            The number of enrollments created.

        """
        enrollments = []
        roster_html = self.cleaned_data['roster']
        items = utils.parse_roster(roster_html)
        for item in items:
            email, fname, lname = item['email'], item['fname'], item['lname']
            user = utils.ensure_user_exists(email, fname=fname, lname=lname)
            student = utils.ensure_student_exists(course.domain, user)
            enrollment = utils.ensure_enrollment_exists(course, student)
            enrollments.append(enrollment)
        return len(enrollments)
