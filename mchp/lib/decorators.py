from allauth.account.decorators import verified_email_required
from allauth.account.models import EmailAddress

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from schedule.models import School

import re

def edu_email_required(func):
    
    @verified_email_required
    def decorator(request, *args, **kwargs):
        email = EmailAddress.objects.filter(
            user=request.user,
            primary=True,
            verified=True,
        )
        if email.exists():
            email = email[0]
        else:
            messages.error(
                request,
                "You need a verified .edu email to visit our site!"
            )
            return redirect(reverse('account_email'))
        p = re.compile('.*(\.edu)$', re.IGNORECASE)
        # they have a verified, primary .edu email address
        if p.match(email.email):
            return func(request, *args, **kwargs)
        else:
            messages.error(
                request,
                "You need a verified .edu email to visit our site!"
            )
            return redirect(reverse('account_email'))
    return decorator
 
def school_required(func):
    
    @edu_email_required
    def decorator(request, *args, **kwargs):
        if request.user.student_exists.__call__():
            student = request.user.student
            deleted, created = School.objects.get_or_create(name='deleted')
            if student.school_id == deleted.id:
                return redirect(reverse('confirm_school')+"?next="+request.get_full_path())
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('confirm_school')+"?next="+request.get_full_path())
    return decorator

def class_required(func):
    
    @school_required
    def decorator(request, *args, **kwargs):
        # we know they have a student because of the previous decorator
        student = request.user.student
        if student.courses.count():
            return func(request, *args, **kwargs)
        else:
            messages.info(
                request,
                "Wait a sec, you haven't added a class to your schedule yet!"
            )
            return redirect(reverse('course_add'))
    return decorator
