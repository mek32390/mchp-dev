from django.core.urlresolvers import reverse
from django.shortcuts import redirect,render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.views.generic.detail import DetailView
from django.views.generic.edit import View
from django.http import HttpResponse, HttpResponseGone
from django.utils.decorators import method_decorator

from allauth.account.decorators import verified_email_required
from allauth.account.models import EmailAddress
from allauth.account.adapter import get_adapter

from schedule.models import School
from user_profile.models import Student, OneTimeFlag
from lib.decorators import school_required
from referral.models import ReferralCode, Referral

import json
import logging
logger = logging.getLogger(__name__)

'''
url: /profile/<number>/slug
url: /profile/<number>
url: /profile/
name: profile
name: my_profile
'''
class ProfileView(DetailView):
    template_name = 'user_profile/profile.html'
    model = Student

    def get_object(self):
        if 'number' in self.kwargs:
            # url: /profile/<number>/
            return get_object_or_404(self.model, id=self.kwargs['number'])
        else:
            # url: /profile/ (logged in users account)
            return get_object_or_404(self.model, user=self.request.user)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = self.object.profile
        return context

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)

profile = ProfileView.as_view()

'''
url: /accounts/settings/
name: account_settings
'''
class AccountSettingsView(View):
    template_name = 'user_profile/account_settings.html'

    def get(self, request, *args, **kwargs):
        ref = ReferralCode.objects.get_referral_code(request.user)
        data = {
            'referral_code': ref.referral_code,
            'referral_link': ref.referral_link,
        }
        return render(request, self.template_name, data)

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(AccountSettingsView, self).dispatch(*args, **kwargs)

account_settings = AccountSettingsView.as_view()

'''
url: /profile/confirm-school/
name: confirm_school
'''
class ConfirmSchoolView(View):
    template_name = 'user_profile/school.html'

    def get(self, request, *args, **kwargs):
        all_schools = School.objects.all().values('name', 'domain', 'pk').order_by('name')
        next = request.GET.get('next', '')
        email = request.user.email.split('@')[1]
        email_parts = email.split('.')[:-1]
        guess_schools = None
        for part in email_parts:
            if part == 'email':
                continue
            schools = School.objects.filter(domain__icontains=part)
            if schools.exists():
                guess_schools = schools[0]
                break

        data = {
            'next': next,
            'schools': all_schools,
            'guess_school': guess_schools
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        school = request.POST.get('school', '')
        school = 1
        school = School.objects.get(pk=school)
        try:
            request.user.student 
        except Student.DoesNotExist:
            Student.objects.create_student(request.user, school)

        # referral stuff
        ref = request.session.get('referrer', '')
        referrer = User.objects.get(pk=ref)
        Referral.objects.refer_user(request.user, referrer, Student.objects.referral_reward)

        next = request.POST.get('next', reverse('course_add'))
        next = reverse('course_add')
        return redirect(next)

    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        return super(ConfirmSchoolView, self).dispatch(*args, **kwargs)

confirm_school = ConfirmSchoolView.as_view()

@require_POST
def get_email(request):
    email = request.POST["email"]
    if request.is_ajax():
        if 'initial_email' in request.session:
            return HttpResponseGone(json.dumps({'message': 'initial_email already set'}), content_type='application/javascript')
        else:
            request.session['initial_email'] = email
            return HttpResponse(json.dumps({}), content_type='application/javascript')
    else:
        request.session['initial_email'] = email
        return redirect('/accounts/signup')

@require_POST
def resend_email(request):
    if request.is_ajax():
        email = request.POST["email"]
        try:
            email_address = EmailAddress.objects.get(email=email)
            get_adapter().add_message(request,
                                      messages.INFO,
                                      'account/messages/'
                                      'email_confirmation_sent.txt',
                                      {'email': email})
            email_address.send_confirmation(request)
        except EmailAddress.DoesNotExist:
            return HttpResponseGone(json.dumps({}), content_type='application/javascript')
        return HttpResponse(json.dumps({}), content_type='application/javascript')
    else:
        return redirect('/')

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

'''
url: /profile/toggle-flag/
name: toggle_flag
'''
class ToggleFlag(View, AjaxableResponseMixin):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            flag = request.POST.get('flag', '')
            flags = OneTimeFlag.objects.default(request.user.student)
            if hasattr(flags, flag):
                setattr(flags, flag, True)
                flags.save()
                return self.render_to_json_response({}, status=200)
            else:
                return self.render_to_json_response({}, status=403)
        else:
            return redirect(reverse('my_profile'))

    def get(self, request, *args, **kwargs):
        return redirect(reverse('my_profile'))

toggle_flag = ToggleFlag.as_view()
