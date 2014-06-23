from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from allauth.account.decorators import verified_email_required

@verified_email_required
def index(request):
    return render_to_response('user_profile/index.html', RequestContext(request))

@verified_email_required
def confirm_school(request):
    return render_to_response('user_profile/school.html', RequestContext(request))

def get_email(request):
    email = request.POST['email']
    request.session['initial_email'] = email
    return redirect('/accounts/signup')
