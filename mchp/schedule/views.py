# from django.shortcuts import render
# from django.core.urlresolvers import reverse
from allauth.account.decorators import verified_email_required
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib import messages
from schedule.forms import CourseCreateForm
import logging
logger = logging.getLogger(__name__)

class CourseCreateView(FormView):
    template_name = 'schedule/course_create.html'
    form_class = CourseCreateForm

    def get_success_url(self):
        # Redirect to previous url - security of getting referer this way?
        return self.request.META.get('HTTP_REFERER', None)

    def form_valid(self, form):
        messages.success(
            self.request,
            "Course Added Successifully!"
        )
        course = form.save(commit=False)
        course.domain = self.request.user.student.school
        course.save()
        return super(CourseCreateView, self).form_valid(form)

    def form_invalid(self, form):
        storage = messages.get_messages(self.request)
        storage.used = True
        return super(CourseCreateView, self).form_invalid(form)

    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        return super(CourseCreateView, self).dispatch(*args, **kwargs)

course_create = CourseCreateView.as_view()

@verified_email_required
def course_remove(request):
    pass

@verified_email_required
def course_add(request):
    pass
