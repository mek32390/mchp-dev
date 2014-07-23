from django.db import models,IntegrityError
from django.core.validators import MinValueValidator, MaxValueValidator

from schedule.utils import clean_domain, US_STATES

from functools import reduce

class School(models.Model):
    domain = models.URLField(validators=[clean_domain])
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=20, blank=True, choices=US_STATES)
    country = models.CharField(max_length=45, blank=True)

    # a list of all school names stored in the database
    def school_list(self):
        return School.objects.all().name

    def document_count(self):
        documents = list(map(lambda student: student.upload_set.count(), 
                        self.student_school.all()))
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

    def student_count(self):
        return self.student_set.count()

    def document_count(self):
        return self.document_set.count()

    def display(self):
        return "{} {} with Instructor {}".format(self.dept,
                                                self.course_number, 
                                                self.professor)

    def __str__(self):
        return "{}{} with prof. {} ".format(self.dept, self.course_number, self.professor)

class Section(models.Model):
    domain = models.ForeignKey('School', related_name='Section_domain')
    dept = models.ForeignKey('Course', related_name='Section_dept')
    course_number = models.ForeignKey('Course', related_name='Section_course_number')
    professor = models.ForeignKey('Course', related_name='Section_professor')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        unique_together = ('domain', 'dept', 'course_number', 'professor', 'start_date', 'end_date')

    def save(self, *args, **kwargs):
        if(self.end_date > self.start_date):
            super().save()
        else:
            raise IntegrityError("Start date must come before end date")

    def __str__(self):
        return "{}{} from {} to {}".format(self.dept, self.course_number, self.start_date,
                                           self.end_date)
