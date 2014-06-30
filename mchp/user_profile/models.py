from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student_user')
    school = models.ForeignKey('schedule.School', related_name='student_school')
    courses = models.ManyToManyField('schedule.Course', db_table='user_profile_enrollment')
    purchased_points = models.IntegerField(default=0)
    earned_points = models.IntegerField(default=0)
    kudos = models.IntegerField(default=0)
    work_credit = models.IntegerField(default=0)
    last_login = models.DateTimeField(auto_now=True)

    def rating(self):
        return self.kudos + self.work_credit

    def total_points(self):
        return self.earned_points + self.purchased_points

    def __str__(self):
        return 'Student: {} goes to {}. Last Login: {}'.format(
            self.user.username, self.school.name, self.last_login
        )

User.student = property(lambda u: Student.objects.get_or_create(user=u)[0])

class UserProfile(models.Model):
    student = models.OneToOneField(Student, related_name='student_profile')

    def __str__(self):
        return 'Profile for {}'.format(self.student.user.username)

    def account_verified(self):
        if self.student.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.student.user.email)
            if len(result):
                return result[0].verified
        return False

Student.profile = property(lambda s: UserProfile.objects.get_or_create(student=s)[0])
