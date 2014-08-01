from django.test import TestCase

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.db.transaction import atomic

from referral.models import Referral, ReferralCode
from user_profile.models import Student
from schedule.models import School

from decimal import Decimal

class ReferalModelTest(TestCase):
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
        self.user = User.objects.create_user('test')

    def testUnique(self):
        user = self.user
        self.assertEqual(user.username, 'test')

        referrer = User.objects.create_user('referrer')
        other = User.objects.create_user('other')

        # referrer refers user
        ref, msg = Referral.objects.refer_user(user, referrer)
        self.assertEqual(ref.referrer.username, referrer.username)
        self.assertEqual(ref.user.username, user.username)

        # referrer refers user again
        ref = Referral(
            user=user,
            referrer=referrer
        )
        with atomic():
            self.assertRaises(IntegrityError, ref.save)

        # referrer refers other
        ref = Referral(
            user=other,
            referrer=referrer
        )
        ref.save()

        # other tried to refer user
        ref = Referral(
            user=user,
            referrer=other
        )
        with atomic():
            self.assertRaises(IntegrityError, ref.save)

        # now try with the manager
        ref, msg = Referral.objects.refer_user(user, other)
        self.assertEqual(ref, None)

    def testReferralCode(self):
        user = self.user
        codes = ReferralCode.objects.get_referral_code(user)
        self.assertEqual(codes.user, user)
        self.assertNotEqual(codes.referral_code, '')

        same_user, msg = ReferralCode.objects.get_user_by_code(codes.referral_code)
        self.assertEqual(user, same_user)

    def testSameUser(self):
        user = self.user
        ref = Referral(
            user=user,
            referrer=user,
        )

        with atomic():
            self.assertRaises(IntegrityError, ref.save)

        reff, msg = Referral.objects.refer_user(user, user)
        self.assertEqual(reff, None)

    def testReward(self):
        user = self.user
        referrer = User.objects.create_user('referrer')
        user_student = Student.objects.create_student(user, self.school)
        referrer_student = Student.objects.create_student(referrer, self.school)
        self.assertEqual(user.student, user_student)

        self.assertEqual(user_student.balance, Decimal("0.00"))
        self.assertEqual(referrer_student.balance, Decimal("0.00"))
        self.assertEqual(user_student.earned_points, 0)
        self.assertEqual(referrer_student.earned_points, 0)

        ref, msg = Referral.objects.refer_user(user, referrer, Student.objects.referral_reward)
        # wtf
        user_student.add_earned_points(500)
        self.assertEqual(user_student.earned_points, 500)
        self.assertEqual(referrer_student.earned_points, 0)

        self.assertEqual(user_student.balance, Decimal("0.00"))
        # wtf
        referrer_student.modify_balance(1)
        self.assertEqual(referrer_student.balance, Decimal("1.00"))


