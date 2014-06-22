from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('user_profile/index.html', RequestContext(request))

def confirm_school(request):
    return render_to_response('user_profile/school.html', RequestContext(request))
