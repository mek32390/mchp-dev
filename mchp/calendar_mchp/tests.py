from django.test import TestCase

from django.contrib.auth.models import User
from django.utils import timezone
# from django.db.utils import IntegrityError
# from django.db.transaction import atomic
from user_profile.models import Student
from schedule.models import School
from calendar_mchp.models import CalendarEvent

class StudentModelTest(TestCase):
    def setUp(self):
        test_uni = {
            'domain': "www.test.edu", 
            'name': "Test University", 
            'phone_number':"(520) 555-5555",
            'address': "413 n What st.", 
            'city':"Test city",
            'state': 'AZ',
            'country': 'USA',
        }
        self.school = School(**test_uni)
        self.school.save()
        student_data = {
            'user': User.objects.create_user('test_dude'),
            'school': self.school,
        }
        self.student = Student(**student_data)
        self.student.save()

    def testCalendarEvent(self):
        test_event = {
            'title': 'test event',
            'allDay': False,
            'start': timezone.now(),
            'url': '',
        }
        event = CalendarEvent(**test_event)
        self.assertEqual(event.title, 'test event')
