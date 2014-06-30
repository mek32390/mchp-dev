from django.shortcuts import render_to_response,redirect,render
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseGone

from allauth.account.decorators import verified_email_required
from allauth.account.models import EmailAddress
from allauth.account.adapter import get_adapter

import json
import logging
logger = logging.getLogger(__name__)

@verified_email_required
def profile(request):
    user = request.user
    try:
       user.student
    except ObjectDoesNotExist:
        return redirect(reverse('confirm_school'))
    else:
        logger.debug(dir(user.student))
    data = {}
    return render(request, 'user_profile/profile.html', data)

@verified_email_required
def confirm_school(request):
    return render_to_response('user_profile/school.html', RequestContext(request))

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
            email_address = EmailAddress.objects.get(
                email=email,
            )
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
