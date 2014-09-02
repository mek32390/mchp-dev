from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.template import Context
from django.db.models import Count
from django.db import IntegrityError
from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone

from lib.decorators import school_required, class_required
from lib.utils import random_mix
from calendar_mchp.models import ClassCalendar, CalendarEvent
from documents.models import Document
from notification.api import add_notification
from schedule.forms import CourseCreateForm, CourseChangeForm
from schedule.models import Course, School, SchoolQuicklink, Section, Department
from schedule.utils import WEEK_DAYS
from user_profile.models import Enrollment

from datetime import datetime
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
    @method_decorator(school_required)
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
        # retrieve the object created before comitting to database
        course = form.save(commit=False)
        # add the domain field
        course.domain = self.student.school
        # try to save course in db
        try:
            course.save()
        except IntegrityError:
            messages.error(
                self.request,
                "This course already exists."
            )
            return super(CourseCreateView, self).form_invalid(form)
        # add student to course
        student = self.student
        enroll = Enrollment(student=student, course=course)
        enroll.save()

        messages.success(
            self.request,
            "Course created successfully!"
        )
        add_notification(
            self.request.user,
            'You created a class! ' + str(course.dept) + ' ' + str(course.course_number)
        )
        add_notification(
            self.request.user,
            'You are now enrolled in ' + str(course.dept) + ' ' + str(course.course_number),
        )
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

        query = ''
        show_results = False
        enrolled_courses = Course.objects.filter(student=self.student).order_by(
            'dept', 'course_number', 'professor'
        )
        # user performed a search
        results = []
        if 'q' in request.GET:
            show_results = True
            query = request.GET['q']
            name = query.replace(' ', '')
            results = Course.objects.filter(
                domain=self.student.school,
                name__icontains=name,
            ).exclude(
                pk__in=enrolled_courses
            ).order_by(
                'dept', 'course_number', 'professor'
            ).annotate(
                student_count = Count('enrollment__student'),
            )

        data = {
            'query': query,
            'enrolled_courses': enrolled_courses,
            'course_results': results,
            'show_results': show_results,
        }

        context_data = Context(self.get_context_data(form=form))
        # context acts like a stack here, update is a push to combine 
        context_data.update(data)
        return render(request, self.template_name, context_data)

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
        enroll = Enrollment(student=student, course=course_to_add)
        enroll.save()

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
                enroll = Enrollment.objects.filter(
                    student=self.student,
                    course=c,
                )
                enroll.delete()
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

'''
url: /school/course/<number>/<slug>/
url: /school/course/<number>/
name: course
'''
class CourseView(DetailView):
    template_name = 'schedule/course.html'
    model = Course

    def get_object(self):
        return get_object_or_404(self.model, id=self.kwargs['number'])

    def get(self, request, *args, **kwargs):
        # if the user types a different slug, and that slug is actually a course that exists
        # redirect to that course instead, otherwise just use the pk value and ignore the slug
        if 'slug' in kwargs and not request.user.is_anonymous():
            slug = self.kwargs['slug']
            number = self.kwargs['number']
            course = Course.objects.filter(name=slug.upper(),
                                           domain=self.request.user.student.school)
            if course.exists() and course[0].pk != int(number):
                kw = {
                    'number': course[0].pk,
                    'slug': slug,
                }
                return redirect(reverse('course_slug', kwargs=kw))
        return super(CourseView, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        docs = self.object.document_set.all(
        ).annotate(
            sold=Count('purchased_document__document'),
        ).extra(select = {
            'review_count': 'SELECT COUNT(*) FROM "documents_documentpurchase"'+ \
            'WHERE ("documents_documentpurchase"."document_id" = "documents_document"."id"' +\
            'AND NOT ("documents_documentpurchase"."review_date" IS NULL))'
        }).order_by('-sold')[:15]

        context['popular_documents'] = docs

        cals = self.object.calendar_courses.filter(
            private=False,
        ).annotate(
            subscriptions=Count('subscribers')
        ).values(
            'pk', 'price', 'description', 'create_date', 'end_date', 'color', 'title',
            'accuracy', 'course__professor', 'owner__user__username', 'subscriptions', 'owner',
            'owner__user__username'
        ).order_by('create_date')[:5]

        for calendar in cals:
            calendar_instance = ClassCalendar.objects.get(pk=calendar['pk'])
            sections = Section.objects.filter(
                course=calendar_instance.course,
                student__pk=calendar['owner'],
            )
            time_string = ''
            for section in sections:
                day_name = WEEK_DAYS[section.day]
                start_date = datetime.combine(datetime.today(), section.start_time)
                end_date = datetime.combine(datetime.today(), section.end_time)

                start_time = timezone.make_aware(start_date, timezone.utc)
                end_time = timezone.make_aware(end_date, timezone.utc)
                start_time = timezone.localtime(start_time, timezone=timezone.get_current_timezone())
                end_time = timezone.localtime(end_time, timezone=timezone.get_current_timezone())
                time_string += day_name[:3] + ' '
                time_string += start_time.strftime('%I%p').lstrip('0') + '-'
                time_string += end_time.strftime('%I%p').lstrip('0') + ' '
            calendar['time'] = time_string
            total_count = CalendarEvent.objects.filter(
                calendar=calendar_instance
            ).count()
            calendar['events'] = total_count

        context['popular_calendars'] = cals
        context['cal_count'] = len(cals)

        # make the bars work
        s_count = self.object.student_set.all().count()
        context['student_count'] = s_count
        all_counts = len(cals) + len(docs) + s_count
        if all_counts:
            context['student_percent'] = (s_count * 100) / all_counts
            context['cal_percent'] = (len(cals) * 100) / all_counts
            context['doc_percent'] = (len(docs) * 100) / all_counts

        if self.student:
            context['student'] = self.student
            context['enrolled'] = Course.objects.filter(
                pk=self.object.pk,
                student=self.student
            ).exists()

        return context

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_anonymous() and self.request.user.student_exists():
            self.student = self.request.user.student
        else:
            self.student = None
        return super(CourseView, self).dispatch(*args, **kwargs)

course = CourseView.as_view()

'''
url: /department/
name: department_list
'''
class DepartmentList(View, AjaxableResponseMixin):
    template_name = 'schedule/course_list.html'

    def POST(self, request, *args, **kwargs):
        return redirect(reverse('profile'))

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            majors = Department.objects.all().order_by('name').values('name')
            data = {
                'majors': list( majors )
            }
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('my_profile'))

    def dispatch(self, *args, **kwargs):
        return super(DepartmentList, self).dispatch(*args, **kwargs)

department_list = DepartmentList.as_view()

'''
url: /school/course/
name: course_list
'''
class CourseListView(ListView):
    template_name = 'schedule/course_list.html'

    def get(self, request, *args, **kwargs):
        if not 'school' in request.GET:
            return super(CourseListView, self).get(self, request, *args, **kwargs)
        else:
            data = {
                'course_list': Course.objects.filter(
                    domain__name__icontains=request.GET['school'].lower()
                ).order_by('dept', 'course_number', 'professor',)
            }
            return render(request, self.template_name, data)

    def get_queryset(self):
        if self.student:
            return Course.objects.filter(
                domain=self.request.user.student.school
            ).order_by('dept', 'course_number', 'professor',)
        else:
            return []

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_anonymous() and self.request.user.student_exists():
            self.student = self.request.user.student
        return super(CourseListView, self).dispatch(*args, **kwargs)

course_list = CourseListView.as_view()

'''
url: /school/<number>/name
name: school
'''
class SchoolView(DetailView):
    template_name = 'schedule/school.html'
    model = School

    def get_object(self):
        return get_object_or_404(self.model, id=self.kwargs['number'])

    def get_context_data(self, **kwargs):
        context = super(SchoolView, self).get_context_data(**kwargs)
        docs = Document.objects.filter(
            course__in = self.object.course_set.all()
        ).annotate(
            sold=Count('purchased_document__document')
        ).extra(select = {
            'review_count': 'SELECT COUNT(*) FROM "documents_documentpurchase"'+ \
            'WHERE ("documents_documentpurchase"."document_id" = "documents_document"."id"' +\
            'AND NOT ("documents_documentpurchase"."review_date" IS NULL))'
        }).order_by('-sold')[:15]

        context['popular_documents'] = docs

        cals = ClassCalendar.objects.filter(
            private=False,
            course__in = self.object.course_set.all()
        ).annotate(
            subscriptions=Count('subscribers')
        ).values(
            'pk', 'price', 'description', 'create_date', 'end_date', 'color', 'title',
            'accuracy', 'course__professor', 'owner__user__username', 'subscriptions', 'owner',
            'owner__user__username', 'course__pk', 'course__dept', 'course__course_number',
        ).order_by('create_date')[:5]

        for calendar in cals:
            calendar_instance = ClassCalendar.objects.get(pk=calendar['pk'])
            sections = Section.objects.filter(
                course=calendar_instance.course,
                student__pk=calendar['owner'],
            )
            time_string = ''
            for section in sections:
                day_name = WEEK_DAYS[section.day]
                start_date = datetime.combine(datetime.today(), section.start_time)
                end_date = datetime.combine(datetime.today(), section.end_time)

                start_time = timezone.make_aware(start_date, timezone.utc)
                end_time = timezone.make_aware(end_date, timezone.utc)
                start_time = timezone.localtime(start_time, timezone=timezone.get_current_timezone())
                end_time = timezone.localtime(end_time, timezone=timezone.get_current_timezone())
                time_string += day_name[:3] + ' '
                time_string += start_time.strftime('%I%p').lstrip('0') + '-'
                time_string += end_time.strftime('%I%p').lstrip('0') + ' '
            calendar['time'] = time_string
            total_count = CalendarEvent.objects.filter(
                calendar=calendar_instance
            ).count()
            calendar['events'] = total_count

        context['popular_calendars'] = cals
        context['cal_count'] = len(cals)
        context['doc_count'] = len(docs)

        s_count = self.object.student_school.all().count()
        context['student_count'] = s_count
        all_counts = len(cals) + len(docs) + s_count
        if all_counts:
            context['student_percent'] = (s_count * 100) / all_counts
            context['cal_percent'] = (len(cals) * 100) / all_counts
            context['doc_percent'] = (len(docs) * 100) / all_counts

        links = SchoolQuicklink.objects.filter(
            domain=self.get_object
        ).order_by('quick_link')
        context['links'] = links
        return context

school = SchoolView.as_view()

'''
url: /school/
name: school_list
'''
class SchoolListView(ListView):
    template_name = 'schedule/school_list.html'
    model = School

    def get_queryset(self):
        return School.objects.all().order_by('name')

school_list = SchoolListView.as_view()

'''
url: /classes/
name: classes
'''
class ClassesView(View):
    template_name = 'schedule/classes.html'

    def get(self, request, *args, **kwargs):
        data = {}
        courses = Course.objects.filter(
            student__user=self.request.user
        ).values(
            'dept', 'course_number', 'professor', 'pk', 'domain', 'name', 'student__user__username',
            'domain__pk', 'domain__name',
        ).annotate(
            doc_count=Count('document')
        )
        for course in courses:
            docs = Document.objects.filter(course=course['pk']).annotate(
                sold=Count('purchased_document__document'),
            ).extra(select = {
                'review_count': 'SELECT COUNT(*) FROM "documents_documentpurchase"'+ \
                'WHERE ("documents_documentpurchase"."document_id" = "documents_document"."id"' +\
                'AND NOT ("documents_documentpurchase"."review_date" IS NULL))',
            }).select_related('course').order_by('-sold')[:15]

            course['documents'] = docs

            act = Document.objects.recent_events(course)

            # get some of the latest people to join your classes
            latest_joins = list(Enrollment.objects.filter(
                course=course['pk']
            ).order_by('join_date')[:5])
            from collections import namedtuple
            Activity = namedtuple('Activity', ['type', 'title', 'time', 'user'])

            # make the list unique
            latest_joins = list(set(latest_joins))

            joins = []
            for join in latest_joins:
                joins.append(Activity('join', join.student.name, join.join_date, join.student))

            both = list(random_mix(act, joins))
            course['activity'] = both
            students = Enrollment.objects.filter(
                course__pk=course['pk']
            )
            course['students'] = students

        data['course_list'] = courses

        return render(request, self.template_name, data)

    @method_decorator(class_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(ClassesView, self).dispatch(*args, **kwargs)

classes = ClassesView.as_view()
