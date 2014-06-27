from django.shortcuts import render
from allauth.account.decorators import verified_email_required

@verified_email_required
def course_create(request):
    data = {'um': 'what'}
    return render(request, 'schedule/course_create.html', data)

def course_remove(request):
    pass

def course_add(request):
    pass
