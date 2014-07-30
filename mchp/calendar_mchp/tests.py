from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
# from django.db.utils import IntegrityError
# from django.db.transaction import atomic
from user_profile.models import Student
from schedule.models import School, Course
from calendar_mchp.models import CalendarEvent#, ClassCalendar

from datetime import datetime, timedelta, timezone as othertimezone

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

        course_data = {
            'dept': 'CSC',
            'course_number': '245',
            'professor': 'mccann',
            'domain': self.school,
        }

        self.course = Course(**course_data)
        self.course.save()
        self.student.courses.add(self.course)

    def testCalendarEvent(self):
        test_event = {
            'title': 'test event',
            'all_day': False,
            'start': timezone.now(),
            'url': '',
        }
        event = CalendarEvent(**test_event)
        self.assertEqual(event.title, 'test event')

    def testsaveCalendar(self):
        self.assertEqual(self.course.dept, 'CSC')
        # now = timezone.now()
        # section_data = {
        #     'course': self.student.courses.all()[0],
        #     'start_date': now,
        #     'end_date': now + timedelta(days=1)
        # }
        # section = Section(**section_data)
        # section.save()
        # self.assertEqual(section.course.dept, 'CSC')
        # self.assertGreater(section.end_date, section.start_date)

        # calendar_data = {
        #     'owner': self.student,
        #     'section':  section,
        # }
        # calendar = ClassCalendar(**calendar_data)
        # calendar.save()
        # self.assertEqual(calendar.owner, self.student)
        # self.assertEqual('CSC 245 Calendar', calendar.title)

        # second_calendar = ClassCalendar(**calendar_data)
        # with atomic():
        #     self.assertRaises(IntegrityError, second_calendar.save)

    def testCalendarTime(self):
        time = datetime.now(othertimezone(timedelta(hours=8)))
        data = {
            'domain': self.school,
            'dept': self.course,
            'course_number': self.course,
            'professor': self.course,
            'start_date': time,
            'end_date': time + timedelta(seconds=5)
        }
        print(data)
