from django.db import models
from schedule.utils import clean_domain

class School(models.Model):
    domain = models.URLField(primary_key=True, validators=[clean_domain])
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return "{} :: {}".format(self.name, self.domain)

class Course(models.Model):
    domain = models.ForeignKey('School')
    dept = models.CharField(max_length=6)
    course_number = models.CharField(max_length=6)
    professor = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("domain", "dept", "course_number", "professor")

    def __str__(self):
        return "{}{} with prof. {} @ {}".format(self.dept, self.course_number, self.professor,
                                                self.domain)

class Section(models.Model):
    pass
