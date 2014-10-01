from django.db import models
from django.db.models import Count
from django.core.validators import MinValueValidator, MaxValueValidator

from schedule.utils import clean_domain, US_STATES
from schedule import managers
from schedule.signals import enrolled

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
    zipcode = models.CharField(max_length=11, blank=True)

    timezone = models.CharField(max_length=50, blank=True)
    lat = models.DecimalField(max_digits=19, decimal_places=15, default=Decimal('00.000'))
    lng = models.DecimalField(max_digits=19, decimal_places=15, default=Decimal('00.000'))

    class Meta:
        ordering = ('name', )

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
    domain = models.ForeignKey(School, related_name='SchoolAlias_domain')
    alias = models.CharField(max_length=100)

    class Meta:
        unique_together = ('domain', 'alias')

    def __str__(self):
        return "Alias for {}: {}".format(self.domain, self.alias)

class SchoolEmail(models.Model):
    school = models.ForeignKey(School, related_name='school_email', null=True, blank=True)
    email_domain = models.CharField(max_length=100)

    class Meta:
        unique_together = ('school', 'email_domain')

    def __str__(self):
        if self.school:
            return "Email for {}: {}".format(self.school.name, self.email_domain)
        else:
            return "Email domain: {} is missing its school".format(self.email_domain)

class Major(models.Model):
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
    domain = models.ForeignKey(School)
    dept = models.CharField(max_length=6)
    course_number = models.IntegerField(
        validators=[MaxValueValidator(99999), MinValueValidator(99)]
    )
    name = models.CharField(max_length=13)
    professor = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)

    course_group = models.IntegerField(blank=True, null=True)

    objects = managers.CourseManager() 

    # managers for 'deleted' cases
    display_objects = DisplayCourseManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.name = self.dept + str(self.course_number)

        # look for similar classes at the same school w/ diff prof
        group_members = Course.objects.filter(
            name=self.name,
            domain=self.domain,
        )
        # if this object doesn't have a group, but there are other similar classes
        if group_members.exists() and not self.course_group:
            # pick a group member
            member = group_members[0]
            course_group = member.course_group
            # see if *that* member has a group
            if course_group:
                self.course_group = course_group
            else:
                # if not, takes the other memeber's pk as the new course_group
                self.course_group = member.pk
                # and assign it to all members in the group
                for group_member in group_members:
                    group_member.course_group = self.course_group
        elif not self.course_group:
            # save the course initially to get its pk
            super(Course, self).save(*args, **kwargs)
            self.course_group = self.pk
            # assign the course_group as pk
            super(Course, self).save(*args, **kwargs)
            return
        super(Course, self).save(*args, **kwargs)

    class Meta:
        unique_together = ("domain", "dept", "course_number", "professor")
        ordering = ['dept', 'course_number', 'professor']

    def students(self):
        return self.enrollment_set.all()

    def student_count(self):
        return len(self.students())

    def document_count(self):
        return self.document_set.count()

    def calendar_count(self):
        return self.calendar_courses.count()

    def display(self):
        return "{} {} with Instructor {}".format(self.dept,
                                                self.course_number, 
                                                self.professor)

    def __str__(self):
        return "{} {}".format(self.dept, self.course_number)

class Enrollment(models.Model):
    student = models.ForeignKey('user_profile.Student', related_name='enrollment')
    course = models.ForeignKey(Course)
    # if the student wants to get emails related to class activity
    receive_email = models.BooleanField(default=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            enrolled.send(sender=self.__class__, enroll=self)
        super(Enrollment, self).save(*args, **kwargs)

    def __str__(self):
        return "Enrolled in {}".format(self.course)

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
        ordering = ['day']

    def __str__(self):
        return "{} from {} to {}".format(WEEK_DAYS[self.day], self.start_time, self.end_time)
