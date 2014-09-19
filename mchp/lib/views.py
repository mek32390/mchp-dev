from django.conf import settings
from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.views.generic import View

class PrivacyPolicyView(View):
    template_name = 'privacy_policy.html'

    def get(self, request, *args, **kwargs):
        data = {
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    # public view
    def dispatch(self, *args, **kwargs):
        return super(PrivacyPolicyView, self).dispatch(*args, **kwargs)

privacy_policy = PrivacyPolicyView.as_view()

class HelpView(View):
    template_name = 'help.html'

    def get(self, request, *args, **kwargs):
        data = {
            'referral_reward': settings.MCHP_PRICING['referral_reward']
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    # public view
    def dispatch(self, *args, **kwargs):
        return super(HelpView, self).dispatch(*args, **kwargs)

help = HelpView.as_view()
