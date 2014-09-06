from django.db import models
from django.db import IntegrityError
from django.contrib.auth.models import User

from referral.utils import generate_referral_code
from referral import managers

import uuid


class ReferralCode(models.Model):
    user = models.ForeignKey(User, primary_key=True, related_name='referal_code')
    referral_code = models.CharField(max_length=13, unique=True)
    referral_link = models.CharField(max_length=32, unique=True)

    objects = managers.ReferralCodeManager()

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
        return "{} has Code: {} :: Link: {}".format(self.user.username, self.referral_code, self.referral_link)

class Referral(models.Model):
    user = models.ForeignKey(User, primary_key=True, related_name='referree')
    referrer = models.ForeignKey(User, related_name='referrer')

    create_date = models.DateTimeField(auto_now_add=True)

    objects = managers.ReferralManager()

    def save(self, *args, **kwargs):
        if self.user == self.referrer:
            raise IntegrityError
        super(Referral, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('user', 'referrer')

    def __str__(self):
        return "{} referred {} on {}".format(self.referrer.username, self.user.username, self.create_date)
