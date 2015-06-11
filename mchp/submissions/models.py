# from django.conf import settings
from django.db import models
from documents.models import BaseDocument
from . import utils


class BaseReview:
    """ Generic submissions base class.

    Attributes
    ----------
    status : django.db.models.CharField
        What is the current review status?
    created : django.db.models.DateTimeField
        When was this review first created?
    updated : django.db.models.DateTimeField
        When was this review last updated?

    """
    INITIAL, FLAGGED, APPROVED, REJECTED = 'i', 'f', 'a', 'r'

    STATUS_CHOICES = (
        (INITIAL, 'Pending initial review'),
        (FLAGGED, 'Flagged for review'),
        (APPROVED, 'Reviewed and approved'),
        (REJECTED, 'Reviewed and rejected'),
    )

    status = models.CharField('review status', max_length=2,
                              choices=STATUS_CHOICES, default=INITIAL)
    created = models.DateTimeField('last updated', auto_now_add=True)
    updated = models.DateTimeField('last updated', auto_now=True)

    class Meta:
        abstract = True

    def greenlit(self):
        "Is this review complete and not rejected?"
        return self.status in (self.FLAGGED, self.APPROVED)


class Review:
    """ Generic submissions base class.

    Attributes
    ----------
    reviewer : django.db.models.ForeignKey
        Who reviewed this document?

    Notes
    -----
    [TODO] Save reviewer.

    """
    reviewer = models.ForeignKey('user_profile.Student')

    # def clean(self, *args, **kwargs):
    #     self.reviewer = django.c
    #     super().clean(*args, **kwargs)


class Syllabus(BaseDocument):
    """ Syllabus.

    Attributes
    ----------
    course : django.db.models.ForeignKey
       A course to which this syllabus is attached.

    """
    course = models.ForeignKey('schedule.Course')

    class Meta:
        verbose_name = 'syllabus'
        verbose_name_plural = 'syllabi'


class Roster:
    """ Roster.

    Attributes
    ----------
    course : django.db.models.ForeignKey
       A course to which this roster is attached.
    html : django.db.models.TextField
        The roster HTML to parse.

    """
    course = models.ForeignKey('schedule.Course')
    html = models.TextField()

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


class SyllabusReview(Review):
    """ Review for a syllabus upload.

    """
    syllabus = models.OneToOneField(Syllabus)


class RosterReview(Review):
    """ Review for a roster submission.

    """
    roster = models.OneToOneField(Roster)


# class EventReview(Review):
#     """ Review for an event set.
#
#     """
#     events = models.OneToOneField(...)
