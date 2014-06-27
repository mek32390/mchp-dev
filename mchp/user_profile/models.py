from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
 

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    def __str__(self):
        return "{}'s profile".format(self.user.username)

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
