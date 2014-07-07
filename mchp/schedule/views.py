from allauth.account.decorators import verified_email_required

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView 
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.template import Context
from django.db.models import Count
from django.http import HttpResponse
from django.core import serializers

from schedule.forms import CourseCreateForm, CourseChangeForm, CourseSearchForm
from schedule.models import Course

from haystack.query import SQ

import logging
import json
logger = logging.getLogger(__name__)

# most views should inherit from this if they submit form data
class _BaseCourseView(FormView):

    def get_success_url(self):
        # Redirect to previous url - security of getting referer this way?
        return self.request.META.get('HTTP_REFERER', None)

    def form_invalid(self, form):
        return super(_BaseCourseView, self).form_invalid(form)

    # dispatch takes care of calling default get and post functions
    # and the decorator will happen in every subclass that doens't override
    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(_BaseCourseView, self).dispatch(*args, **kwargs)

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)

    I stole this right from the django website.
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def ajax_messages(self):
        django_messages = []

        for message in messages.get_messages(self.request):
            django_messages.append({
                "level": message.level,
                "message": message.message,
                "extra_tags": message.tags,
            })
        return django_messages

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response

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
        # retrieve the object created before comitting to database
        course = form.save(commit=False)
        # add the domain field
        course.domain = self.student.school
        # save course in db
        course.save()
        # add student to course
        student = self.student
        student.courses.add(course)

        return super(CourseCreateView, self).form_valid(form)

course_create = CourseCreateView.as_view()

class CourseAddView(_BaseCourseView, AjaxableResponseMixin):
    template_name = 'schedule/course_add.html'
    form_class = CourseChangeForm

    # get search results (if requested), 
    # and show search box and currently enrolled courses
    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        existing_courses = []
        query = ''
        show_results = False
        enrolled_courses = Course.objects.filter(student=self.student).order_by(
            'dept', 'course_number', 'professor'
        )
        # user performed a search
        if 'q' in request.GET:
            show_results = True
            query = request.GET['q']
            if query != '':
                existing_courses = self.search_classes(request, enrolled_courses)

        data = {
            'query': query,
            'enrolled_courses': enrolled_courses,
            'course_results': existing_courses,
            'show_results': show_results,
        }

        context_data = Context(self.get_context_data(form=form))
        # context acts like a stack here, update is a push to combine 
        context_data.update(data)
        return render(request, self.template_name, context_data)

    # using haystack
    def search_classes(self, request, already_enrolled):
        # haystack stuff
        form = CourseSearchForm(request.GET)
        sq = SQ()

        # add a filter for already enrolled classes
        for course in already_enrolled:
            sq.add(~SQ(
                dept=course.dept, 
                course_number=course.course_number,
                professor=course.professor,
            ), SQ.OR)

        # perform search 
        if not already_enrolled:
            courses = form.search().filter()
        else:
            courses = form.search().filter(sq)

        # annotate the results with number of students in each course
        # first get all primary keys from the search results
        pks = list(map((lambda c: c.pk), courses))
        course_list = Course.objects.filter(
            pk__in=pks, 
            # filter out other schools
            domain=self.student.school
        )\
        .order_by('dept', 'course_number', 'professor')\
        .annotate(student_count = Count('student'))

        return course_list

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Failed to add course."
        )
        if self.request.is_ajax():
            return self.render_to_json_response(dict(form.errors.items()), status=400)
        else:
            return self.get(self.request)

    def form_valid(self, form):
        # save model manually, don't call save form
        # form.save() would overwrite current classes instead of appending
        student = self.student
        course_to_add = form.cleaned_data['courses'][0]
        student.courses.add(course_to_add)

        messages.success(
            self.request,
            "Course added successfully!"
        )

        if self.request.is_ajax():
            course = serializers.serialize('json', [course_to_add])
            data = {
                'messages': self.ajax_messages(),
                'course': course,
            }
            return self.render_to_json_response(data)
        else:
            return super(CourseAddView, self).form_valid(form)

course_add = CourseAddView.as_view()

class CourseRemoveView(_BaseCourseView, AjaxableResponseMixin):
    form_class = CourseChangeForm

    def get(self, request):
        return redirect(reverse('course_add'))

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Failed to delete course"
        )
        if self.request.is_ajax():
            return self.render_to_json_response(dict(form.errors.items()), status=400)
        else:
            return redirect(reverse('course_add'))

    def form_valid(self, form):
        if self.request.is_ajax():
            course = form.cleaned_data['courses']
            for c in course:
                self.student.courses.remove(c)
            messages.success(
                self.request,
                "Course removed successfully"
            )
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data)
        else:
            return redirect(reverse('course_add'))

course_remove = CourseRemoveView.as_view()
