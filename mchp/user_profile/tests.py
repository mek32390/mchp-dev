from django.test import TestCase

from django.contrib.auth.models import User
# from django.db.utils import IntegrityError
# from django.db.transaction import atomic
from user_profile.models import Student
from schedule.models import School

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

    def testReducePoints(self):
        student = self.student
        self.assertEqual(student.total_points(), 0)
        self.assertEqual(student.reduce_points(-1), None)
        self.assertEqual(student.reduce_points(0), 0)
        self.assertEqual(student.reduce_points(1), None)

        student.add_earned_points(5)
        self.assertEqual(student.total_points(), 5)

        student.add_purchased_points(5)
        self.assertEqual(student.earned_points, 5)
        self.assertEqual(student.purchased_points, 5)
        self.assertEqual(student.total_points(), 10)

        self.assertEqual(student.reduce_points(1), 9)
        self.assertEqual(student.total_points(), 9)
        self.assertEqual(student.earned_points, 5)
        self.assertEqual(student.purchased_points, 4)

        self.assertEqual(student.reduce_points(5), 4)
        self.assertEqual(student.total_points(), 4)
        self.assertEqual(student.earned_points, 4)
        self.assertEqual(student.purchased_points, 0)

        self.assertEqual(student.reduce_points(5), None)
        self.assertEqual(student.reduce_points(4), 0)
