from django.test import TestCase

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.db.transaction import atomic

from referral.models import Referral, ReferralCode

class ReferalModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test')

    def testUnique(self):
        user = self.user
        self.assertEqual(user.username, 'test')

        referrer = User.objects.create_user('referrer')
        other = User.objects.create_user('other')

        # referrer refers user
        ref = Referral.objects.refer_user(user, referrer)
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
        ref = Referral.objects.refer_user(user, other)
        self.assertEqual(ref, None)

    def testReferralCode(self):
        user = self.user
        codes = ReferralCode.objects.get_referral_code(user)
        self.assertEqual(codes.user, user)
        self.assertNotEqual(codes.referral_code, '')

        same_user = ReferralCode.objects.get_user_by_code(codes.referral_code)
        self.assertEqual(user, same_user)

    def testSameUser(self):
        user = self.user
        ref = Referral(
            user=user,
            referrer=user,
        )

        with atomic():
            self.assertRaises(IntegrityError, ref.save)

        self.assertEqual(Referral.objects.refer_user(user, user), None)


