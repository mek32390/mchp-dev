# from django.shortcuts import render
# from django.core.urlresolvers import reverse
from allauth.account.decorators import verified_email_required
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib import messages
from schedule.forms import CourseCreateForm, CourseAddForm
import logging
logger = logging.getLogger(__name__)

class _BaseCourseView(FormView):

    def get_success_url(self):
        # Redirect to previous url - security of getting referer this way?
        return self.request.META.get('HTTP_REFERER', None)

    def form_invalid(self, form):
        return super(_BaseCourseView, self).form_invalid(form)

    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        return super(_BaseCourseView, self).dispatch(*args, **kwargs)

class CourseCreateView(_BaseCourseView):
    template_name = 'schedule/course_create.html'
    form_class = CourseCreateForm

    def form_valid(self, form):
        messages.success(
            self.request,
            "Course created successifully!"
        )
        course = form.save(commit=False)
        course.domain = self.request.user.student.school
        course.save()
        return super(CourseCreateView, self).form_valid(form)

course_create = CourseCreateView.as_view()

class CourseAddView(_BaseCourseView):
    template_name = 'schedule/course_add.html'
    form_class = CourseAddForm

    def form_valid(self, form):
        messages.success(
            self.request,
            "Course added successifully!"
        )
        return super(CourseAddView, self).form_valid(form)

course_add = CourseAddView.as_view()

@verified_email_required
def course_remove(request):
    pass
