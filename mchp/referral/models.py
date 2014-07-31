from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

from referral.utils import generate_referral_code

import uuid

class ReferralCodeManager(models.Manager):
    # get or create the referral codes for a user
    def get_referral_code(self, user):
        ref_code = ReferralCode.objects.filter(user=user)
        if ref_code.exists():
            return ref_code[0]
        else:
            ref_code = ReferralCode(user=user)
            ref_code.save()
            return ref_code
        
    def get_user_by_code(code):
        user = ReferralCode.objects.filter(
            Q(referral_link=code) |
            Q(referral_code=code)
        )
        if user.exists():
            return user[0]
        else:
            return None

class ReferralCode(models.Model):
    user = models.ForeignKey(User, primary_key=True, related_name='referal_code')
    referral_code = models.CharField(max_length=13, unique=True)
    referral_link = models.CharField(max_length=32, unique=True)

    objects = ReferralCodeManager()

    def save(self, *args, **kwargs):
        ref_code = generate_referral_code()
        while ReferralCode.objects.filter(referral_code=ref_code).exists():
            ref_code = generate_referral_code()
        link_code = uuid.uuid4().hex[:15]
        while ReferralCode.objects.filter(referral_link=link_code).exists():
            link_code = uuid.uuid4().hex[:15]

        self.referral_code = ref_code
        self.referral_link = link_code
        super(ReferralCode, self).save(*args, **kwargs)

    def __str__(self):
        return "Code: {} :: Link: {}".format(self.referral_code, self.referral_link)

class Referral(models.Model):
    user = models.ForeignKey(User, primary_key=True, related_name='referree')
    referrer = models.ForeignKey(User, related_name='referrer')

    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'referrer')

    def __str__(self):
        return "referral made {}".format(self.create_date)
