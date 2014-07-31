from django.conf import settings
from referral.models import ReferralCode

class ReferralMiddleware():
    def process_request(self, request):
        # if the user clicked a link with a referral in it
        if settings.REF_GET_PARAMETER in request.GET:
            referral_link = request.GET.get(settings.REF_GET_PARAMETER, None)
            # find out who owns that link code
            referrer = ReferralCode.objects.get_user_by_code(referral_link)
            # add it in the session so it can be referenced
            if not referrer is None:
                request.session[settings.REF_SESSION_KEY] = referrer.pk


