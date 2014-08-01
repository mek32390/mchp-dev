from django.db import models

import referral.models

class ReferralCodeManager(models.Manager):
    # get or create the referral codes for a user
    def get_referral_code(self, user):
        ref_code = referral.models.ReferralCode.objects.filter(user=user)
        if ref_code.exists():
            return ref_code[0]
        else:
            ref_code = referral.models.ReferralCode(user=user)
            ref_code.save()
            return ref_code
        
    def get_user_by_code(self, code):
        codes = referral.models.ReferralCode.objects.filter(
            referral_code=code
        )
        if codes.exists():
            return codes[0].user, ""
        else:
            return None, "We couldn't find that referral code!"

    def get_user_by_link(self, link):
        links = referral.models.ReferralCode.objects.filter(
            referral_link=link
        )
        if links.exists():
            return links[0].user, ""
        else:
            return None, "We couldn't find that referral link!"

class ReferralManager(models.Manager):
    def refer_user(self, user, referrer, reward=(lambda x,y: x)):
        if referral.models.Referral.objects.filter(user=user).exists():
            return None, "You have already redeemed a referral"
        else:
            if user == referrer:
                return None, "You can't refer yourself!"
            ref = referral.models.Referral(
                user=user,
                referrer=referrer,
            )
            ref.save()
            reward(user, referrer)
            return ref, "Referral Code redeemed!"
