from django.db import models
from django.contrib.auth.models import User

from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount

from documents.models import Upload,DocumentPurchase

from functools import reduce
import urllib
import json

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student_user')

    school = models.ForeignKey('schedule.School', related_name='student_school')
    courses = models.ManyToManyField('schedule.Course', db_table='user_profile_enrollment',
                                     blank=True)

    friends = models.ManyToManyField('self', db_table='user_profile_friends', blank=True)

    purchased_points = models.IntegerField(default=0)
    earned_points = models.IntegerField(default=0)
    kudos = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    def name(self):
        if self.user.first_name:
            return self.user.first_name + " " + self.user.last_name
        else:
            return self.user.username

    def work_score(self):
        return\
                Upload.objects.filter(owner=self).count()\
                + self.courses.count()\
                + DocumentPurchase.objects.filter(student=self).count()\
                + self.sales()\

    def rating(self):
        return 8
        return self.kudos + self.work_score()

    # things to do with points
    def total_points(self):
        return self.earned_points + self.purchased_points

    def add_purchased_points(self, points):
        self.purchased_points = self.purchased_points + points
        self.save()
        
    def add_earned_points(self, points):
        self.earned_points = self.earned_points + points
        self.save()

    def reduce_points(self, points):
        if self.total_points() < points or points < 0:
            return None
        if self.purchased_points - points < 0:
            points = points - self.purchased_points
            self.purchased_points = 0
            self.earned_points = self.earned_points - points
        else:
            self.purchased_points = self.purchased_points - points
        self.save()
        return self.total_points();

    # this returns the total number of documents that this student has sold
    # e.x. they uploaded two docs and the first was bought 1 time,
    # and the other 2 times, this function returns 3
    def sales(self):
        all_uploads = Upload.objects.filter(owner=self)
        counts = map(lambda upload: upload.document.purchase_count(), all_uploads)
        return reduce(lambda doc1, doc2: doc1 + doc2, counts)

    def __str__(self):
        return 'Student: {} goes to {}. Joined: {}'.format(
            self.user.username, self.school.name, self.create_date
        )

User.student = property(lambda u: Student.objects.get(user=u))

class UserProfile(models.Model):
    student = models.OneToOneField(Student, related_name='student_profile')
    pic = models.ImageField(upload_to="profile_pic/", blank=True, null=True)
 
    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user=self.student.user, provider='facebook')
     
        if len(fb_uid):
            request = 'https://graph.facebook.com/{}/picture/?width=800&redirect=false'.format(fb_uid[0].uid)
            response = urllib.request.urlopen(request)
            obj = json.loads(response.readall().decode('utf-8'))
            return obj['data']['url']
        elif self.pic:
            return self.pic.url
        else:
            return "https://s3-us-west-2.amazonaws.com/mchpstatic/Circle+Icons+/png/128px/profile.png"

    def __str__(self):
        return 'Profile for {}'.format(self.student.user.username)

    def account_verified(self):
        if self.student.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.student.user.email)
            if len(result):
                return result[0].verified
        return False

Student.profile = property(lambda s: UserProfile.objects.get_or_create(student=s)[0])

class StudentQuicklink(models.Model):
    student = models.ForeignKey('Student', related_name='userlink_student')
    quick_link = models.URLField()
    name = models.CharField(max_length=40)
    follows = models.ForeignKey('self',
                               blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('student', 'quick_link')

    # return the first ql
    def first(self, student):
        return self.objects.filter(student=student, follows=None)

    def rest(self):
        return self.objects.select_related('self').get(id=id)

    def __str__(self):
        return "{} has link to {}".format(self.student.user.username, self.quick_link)
