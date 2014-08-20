from django.db import models
from django.db.models import Count
from django.core.validators import MinValueValidator, MaxValueValidator

from schedule.utils import clean_domain, US_STATES

from functools import reduce
from decimal import Decimal

class School(models.Model):
    domain = models.URLField(validators=[clean_domain])
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)

    address = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=20, blank=True, choices=US_STATES)
    country = models.CharField(max_length=45, blank=True)
    zip_code = models.CharField(max_length=11, blank=True)

    timezone = models.CharField(max_length=50, blank=True)
    lat = models.DecimalField(max_digits=19, decimal_places=15, default=Decimal('00.000'))
    lng = models.DecimalField(max_digits=19, decimal_places=15, default=Decimal('00.000'))

    # a list of all school names stored in the database
    def school_list(self):
        return School.objects.all().name

    def document_count(self):
        s = self.student_school.all().annotate(
            count = Count('upload')
        )
        documents = list(map(lambda student: student.count, s))
        if not documents:
            return 0
        return reduce(lambda c1, c2: c1 + c2, documents)

    def __str__(self):
        return "{} :: {}".format(self.name, self.domain)

class SchoolQuicklink(models.Model):
    domain = models.ForeignKey('School', related_name='SchoolQuicklink_domain')
    quick_link = models.URLField()
    name = models.CharField(max_length=40)

    class Meta:
        unique_together = ('domain', 'quick_link')

    def __str__(self):
        return "Quicklink: {} :: {}".format(self.domain, self.quick_link)

class SchoolAlias(models.Model):
    domain = models.ForeignKey('School', related_name='SchoolAlias_domain')
    alias = models.CharField(max_length=12)

    class Meta:
        unique_together = ('domain', 'alias')

    def __str__(self):
        return "Alias for {}: {}".format(self.domain, self.alias)

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)

class DisplayCourseManager(models.Manager):
    def get_queryset(self):
        deleted_school, created = School.objects.get_or_create(
            domain='deleted.edu', name='deleted')
        return super(DisplayCourseManager, self).get_queryset().exclude(
           domain = deleted_school
        )

class Course(models.Model):
    domain = models.ForeignKey('School')
    dept = models.CharField(max_length=6)
    course_number = models.IntegerField(
        validators=[MaxValueValidator(99999), MinValueValidator(99)]
    )
    name = models.CharField(max_length=13)
    professor = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)

    # managers for 'deleted' cases
    objects = models.Manager() # The default manager.
    display_objects = DisplayCourseManager()

    def save(self, *args, **kwargs):
        self.name = self.dept + str(self.course_number)
        super(Course, self).save(*args, **kwargs)

    class Meta:
        unique_together = ("domain", "dept", "course_number", "professor")

    def students(self):
        return self.student_set.all().select_related()

    def student_count(self):
        return self.student_set.count()

    def document_count(self):
        return self.document_set.count()

    def display(self):
        return "{} {} with Instructor {}".format(self.dept,
                                                self.course_number, 
                                                self.professor)

    def __str__(self):
        return "{} {}".format(self.dept, self.course_number)

from schedule.utils import WEEK_DAYS
class Section(models.Model):
    course = models.ForeignKey(Course, related_name="sections")
    student = models.ForeignKey('user_profile.Student', related_name='student_sections')

    week_day_list = list(zip(range(10), WEEK_DAYS))
    day = models.PositiveSmallIntegerField(max_length=10, choices=week_day_list)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ("student", "course", "day")

    def __str__(self):
        return "{} from {} to {}".format(WEEK_DAYS[self.day], self.start_time, self.end_time)
