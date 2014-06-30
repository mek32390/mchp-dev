from django.shortcuts import redirect,render
from django.template import Context
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseGone

from allauth.account.decorators import verified_email_required
from allauth.account.models import EmailAddress
from allauth.account.adapter import get_adapter

from schedule.models import School
from user_profile.models import Student, UserProfile

import json
import logging
logger = logging.getLogger(__name__)

@verified_email_required
def profile(request):
    student = Student.objects.filter(user=request.user)
    data = {}
    if not len(student):
        return redirect(reverse('confirm_school')+"?next="+request.get_full_path())
    else:
        return render(request, 'user_profile/profile.html', Context(data))

# FIXME: wow this is bad
# this should at least be a form view
@verified_email_required
def confirm_school(request):
    if request.method == 'POST':
        if 'school' in request.POST:
            logger.debug(request)
            school = request.POST['school']
            school = School.objects.get(domain=school)
            logger.debug(school)
            student, created = Student.objects.get_or_create(
                user=request.user, school=school
            )
            logger.debug(student)
            if not created:
                student.save()
                profile = UserProfile(student=student)
                profile.save()

            if 'next' in request.POST and request.POST['next'] != '':
                return redirect(request.POST['next'])
            else:
                return redirect('/profile/')

    schools = School.objects.all().values('name', 'domain')
    if 'next' in request.GET:
        next_page = request.GET['next']
        data = {'schools': schools, 'next': next_page}
    else:
        data = {'schools': schools}
    return render(request, 'user_profile/school.html', Context(data))

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
