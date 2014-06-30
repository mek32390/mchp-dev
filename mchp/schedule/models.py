from django.db import models,IntegrityError
from django.core.validators import MinValueValidator, MaxValueValidator
from schedule.utils import clean_domain

class School(models.Model):
    domain = models.URLField(primary_key=True, validators=[clean_domain])
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=25, blank=True)

    # a list of all school names stored in the database
    def school_list(self):
        return School.objects.all().name

    def __str__(self):
        return "{} :: {}".format(self.name, self.domain)

class SchoolQuicklink(models.Model):
    domain = models.ForeignKey('School', related_name='SchoolQuicklink_domain')
    quick_link = models.URLField()

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

class Course(models.Model):
    domain = models.ForeignKey('School')
    dept = models.CharField(max_length=6)
    course_number = models.IntegerField(
        validators=[MaxValueValidator(99999), MinValueValidator(99)]
    )
    professor = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("domain", "dept", "course_number", "professor")

    def __str__(self):
        return "{}{} with prof. {} @ {}".format(self.dept, self.course_number, self.professor,
                                                self.domain)

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
