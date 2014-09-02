import pytz

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

class TimezoneMiddleware(object):
    # activate the current time zone for the student according to their school time zone
    def process_request(self, request):
        if not request.user.is_anonymous() and request.user.student_exists():
            tz = request.user.student.school.timezone
            if tz:
                timezone.activate(pytz.timezone(tz))
            else:
                timezone.deactivate()

class UserMigrationMiddleware(object):

    def process_request(self, request):
        # first try their session (when they enter on the landing page)
        email = request.session.get('initial_email', None)
        # then try to see if this was a login attempt
        if not email:
            email = request.POST.get('login', None)
        # no use in doing queries with None
        if not email:
            return 
        # try to match w/ users who exist from old site
        user = User.objects.filter(
            password ='blank',
            email=email,
        )
        # force old users to make a new password
        if user.exists():
            request.session['migration'] = True 
            request.session.pop('initial_email', None)
            return redirect(reverse('account_reset_password'))
