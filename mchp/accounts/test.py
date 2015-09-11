from allauth import app_settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import perform_login
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import ObjectDoesNotExist


class AccountAdapter(DefaultAccountAdapter):
    def is_auto_signup_allowed(self, request, sociallogin):
        return True

    def pre_social_login(self, request, sociallogin):
        user = sociallogin.account.user
        if user.id:
            return
        try:
            existing_user = User.objects.get(email=user.email)
        except ObjectDoesNotExist:
            pass
        else:
            perform_login(request, existing_user, app_settings.EmailVerificationMethod.NONE)