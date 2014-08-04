from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic.edit import View

from lib.decorators import school_required
from user_profile.models import Student
from referral.models import ReferralCode, Referral

import json

'''
url: /referral/redeem/
name: referral_redeem
'''
class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.

    I stole this right from the django website.
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def ajax_messages(self):
        django_messages = []

        for message in messages.get_messages(self.request):
            django_messages.append({
                "level": message.level,
                "message": message.message,
                "extra_tags": message.tags,
            })
        return django_messages

class RedeemView(View, AjaxableResponseMixin):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('my_profile'))

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            code = request.POST.get('referral_code', '')
            referrer, message = ReferralCode.objects.get_user_by_code(code)
            if referrer:
                referral, msg = Referral.objects.refer_user(request.user, referrer,
                                                            Student.objects.referral_reward)
                if referral:
                    messages.success(
                        self.request,
                        msg
                    )
                else:
                    messages.error(
                        self.request,
                        msg
                    )
            else:
                messages.error(
                    self.request,
                    message,
                )

            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data)
        else:
            return redirect(reverse('my_profile'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        return super(RedeemView, self).dispatch(*args, **kwargs)

redeem = RedeemView.as_view()
