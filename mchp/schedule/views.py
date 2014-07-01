from allauth.account.decorators import verified_email_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib import messages

from schedule.forms import CourseCreateForm, CourseAddForm
from schedule.models import Course

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
    
    def get_success_url(self):
        return reverse('course_add')

    def form_valid(self, form):
        messages.success(
            self.request,
            "Course created successfully!"
        )
        course = form.save(commit=False)
        course.domain = self.request.user.student.school
        course.save()
        return super(CourseCreateView, self).form_valid(form)

course_create = CourseCreateView.as_view()

class CourseAddView(_BaseCourseView):
    template_name = 'schedule/course_add.html'
    form_class = CourseAddForm

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        existing_courses = Course.objects.filter(
            domain = self.request.user.student.school
        )

        enrolled_courses = self.request.user.student.courses.all()
        course_data = {
            'enrolled_courses': enrolled_courses,
            'course_list': existing_courses,
        }

        context_data = self.get_context_data(form=form)
        context = dict(context_data.items() | course_data.items())
        logger.debug(context)
        return render(request, self.template_name, context)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Failed to add course."
        )
        return self.get(self.request)

    def form_valid(self, form):
        messages.success(
            self.request,
            "Course added successfully!"
        )
        student = self.request.user.student
        logger.debug(student)
        logger.debug(self.request)
        return super(CourseAddView, self).form_valid(form)

course_add = CourseAddView.as_view()

@verified_email_required
def course_remove(request):
    pass
