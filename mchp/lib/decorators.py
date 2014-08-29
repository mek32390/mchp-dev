from allauth.account.decorators import verified_email_required

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
 
def school_required(func):
    
    @verified_email_required
    def decorator(request, *args, **kwargs):
        if request.user.student_exists.__call__():
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
