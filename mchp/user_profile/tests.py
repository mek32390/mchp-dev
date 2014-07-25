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

    def testStudentBalance(self):
        from decimal import Decimal
        student = self.student
        self.assertEqual(student.balance, 0)
        self.assertEqual(student.balance, Decimal(0))
        self.assertEqual(student.balance, Decimal('0'))
        self.assertEqual(student.balance, Decimal('0.00'))
        self.assertEqual(student.display_balance(), '0.00')

        student.modify_balance(1)
        self.assertEqual(student.balance, Decimal(1))
        self.assertEqual(student.display_balance(), '1.00')

        student.modify_balance('1.000')
        self.assertEqual(student.balance, Decimal(2))
        self.assertEqual(student.display_balance(), '2.00')

        student.modify_balance('1.001')
        self.assertEqual(student.balance, Decimal('3.001'))
        self.assertEqual(student.display_balance(), '3.00')

        student.modify_balance('.0039')
        self.assertEqual(student.balance, Decimal('3.0049'))
        self.assertEqual(student.display_balance(), '3.00')

        student.modify_balance('.0001')
        self.assertEqual(student.balance, Decimal('3.005'))
        self.assertEqual(student.display_balance(), '3.00')

        student.modify_balance('.0001')
        self.assertEqual(student.balance, Decimal('3.0051'))
        self.assertEqual(student.display_balance(), '3.01')

        student.modify_balance('.0010')
        self.assertEqual(student.balance, Decimal('3.0061'))
        self.assertEqual(student.display_balance(), '3.01')

        student.modify_balance('.00001')
        self.assertEqual(student.balance, Decimal('3.0061'))
        self.assertEqual(student.display_balance(), '3.01')
        
        student.modify_balance('-4')
        self.assertEqual(student.balance, Decimal('-.9939'))
        self.assertEqual(student.display_balance(), '-0.99')
        
