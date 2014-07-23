from django.core.urlresolvers import reverse
from django.shortcuts import redirect
 
def school_required(func):
    
    def decorator(request, *args, **kwargs):
        if request.user.student_exists:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('confirm_school')+"?next="+request.get_full_path())
    return decorator
