from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Count
from django.db import IntegrityError
from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone

from lib.decorators import school_required, class_required
from lib.utils import random_mix
from calendar_mchp.models import ClassCalendar, CalendarEvent, Subscription
from documents.models import Document
from notification.api import add_notification
from schedule.forms import CourseCreateForm
from schedule.models import Course, School, SchoolQuicklink, Section, Major, Enrollment
from schedule.utils import WEEK_DAYS
from user_profile.models import Student

from datetime import datetime, timedelta
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
        admin_user = Student.get_admin()

        # create public calendar
        calendar_data = {
            'course': course,
            'owner': admin_user,
            'description': '',
            'end_date': timezone.now() + timedelta(days=365 * 5), # off-setting to 5 years
            'private': False,
            'primary': True,
        }

        calendar = ClassCalendar(**calendar_data)
        calendar.save()

        course.enroll(self.student)

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

    # get search results (if requested), 
    # and show search box and currently enrolled courses
    def get(self, request, *args, **kwargs):
        query = ''
        show_results = False
        enrolled_courses = Course.objects.get_classes_for(self.student)
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

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            course_id = request.POST.get('course', None)
            course = Course.objects.filter(
                pk=course_id
            )
            if course.exists():
                course = course[0]
            else:
                messages.error(
                    self.request,
                    "Failed to add course. Not found."
                )
                return self.render_to_json_response({}, status=400)

            course.enroll(self.student)

            messages.success(
                self.request,
                "Course added successfully!"
            )
            course = serializers.serialize('json', [course])
            data = {
                'messages': self.ajax_messages(),
                'course': course,
            }
            return self.render_to_json_response(data)
        else:
            return redirect(reverse('course_add')) 

course_add = CourseAddView.as_view()

class CourseRemoveView(_BaseCourseView, AjaxableResponseMixin):

    def get(self, request):
        return redirect(reverse('course_add'))

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            course_id = request.POST.get('course', None)
            course = Course.objects.filter(
                pk=course_id
            )
            if course.exists():
                course = course[0]
            else:
                messages.error(
                    self.request,
                    "Failed to remove course"
                )
                return self.render_to_json_response({}, status=400)
            enroll = Enrollment.objects.filter(
                student=self.student,
                course=course,
            )
            enroll.delete()

            # Unsubscribing from all calendars
            subscriptions = Subscription.objects.filter(student=self.student, calendar__course=course)
            subscriptions.delete()

            # Removing student calendars (events will cascade delete too)
            calendars = ClassCalendar.objects.filter(owner=self.student, course=course)
            calendars.delete()

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
class CourseView(View):
    template_name = 'schedule/course.html'
    model = Course

    def get_object(self):
        if hasattr(self, 'object'):
            return self.object
        else:
            self.object = get_object_or_404(self.model, id=self.kwargs['number'])
        return self.object

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        course = self.get_object()
        context = {'course': course}

        courses = Course.objects.filter(
            course_group=course.course_group,
        )
        docs = []
        cals = []
        student_count = 0
        for course in courses:
            course_docs = course.document_set.all(
            ).annotate(
                sold=Count('purchased_document__document'),
            ).extra(select = {
                'review_count': 'SELECT COUNT(*) FROM "documents_documentpurchase"'+ \
                'WHERE ("documents_documentpurchase"."document_id" = "documents_document"."id"' +\
                'AND NOT ("documents_documentpurchase"."review_date" IS NULL))'
            }).order_by('-sold')[:15]
            docs.append(course_docs)

            course_cals = course.calendar_courses.filter(
                private=False,
            ).annotate(
                subscriptions=Count('subscribers')
            ).values(
                'pk', 'description', 'create_date', 'end_date', 'color', 'title',
                'course__professor', 'owner__user__username', 'subscriptions', 'owner',
                'owner__user__username'
            ).order_by('create_date')[:5]

            for calendar in course_cals:
                calendar_instance = ClassCalendar.objects.get(pk=calendar['pk'])
                sections = Section.objects.filter(
                    course=calendar_instance.course,
                    student__pk=calendar['owner'],
                ).order_by('day')
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
            cals.append(course_cals)
            student_count = student_count + course.student_count()

        docs = [doc for course_doc in docs for doc in course_doc]
        context['popular_documents'] = docs
        context['doc_count'] = len(docs)

        cals = [cal for course_cal in cals for cal in course_cal]
        context['popular_calendars'] = cals
        context['cal_count'] = len(cals)

        # make the bars work
        s_count = course.student_count()
        context['student_count'] = s_count
        all_counts = len(cals) + len(docs) + s_count
        if all_counts:
            context['student_percent'] = (s_count * 100) / all_counts
            context['cal_percent'] = (len(cals) * 100) / all_counts
            context['doc_percent'] = (len(docs) * 100) / all_counts

        if self.student:
            course = self.get_object()
            context['student'] = self.student
            context['enrolled'] = Enrollment.objects.filter(
                course__pk__in=[c.pk for c in courses],
                student=self.student
            ).exists()
        context['student_count'] = student_count

        return context

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_anonymous() and self.request.user.student_exists():
            self.student = self.request.user.student
        else:
            self.student = None
        return super(CourseView, self).dispatch(*args, **kwargs)

course = CourseView.as_view()

'''
url: /major/
name: major_list
'''
class MajorList(View, AjaxableResponseMixin):
    template_name = 'schedule/course_list.html'

    def POST(self, request, *args, **kwargs):
        return redirect(reverse('profile'))

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            majors = Major.objects.all().order_by('name').values('name')
            data = {
                'majors': list( majors )
            }
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('my_profile'))

    def dispatch(self, *args, **kwargs):
        return super(MajorList, self).dispatch(*args, **kwargs)

major_list = MajorList.as_view()

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
        }).order_by('-sold')

        context['popular_documents'] = docs

        cals = ClassCalendar.objects.filter(
            private=False,
            course__in = self.object.course_set.all()
        ).annotate(
            subscriptions=Count('subscribers')
        ).values(
            'pk', 'description', 'create_date', 'end_date', 'color', 'title',
            'course__professor', 'owner__user__username', 'subscriptions', 'owner',
            'owner__user__username', 'course__pk', 'course__dept', 'course__course_number',
        ).order_by('-subscriptions')

        for calendar in cals:
            calendar_instance = ClassCalendar.objects.get(pk=calendar['pk'])
            sections = Section.objects.filter(
                course=calendar_instance.course,
                student__pk=calendar['owner'],
            ).order_by('day')
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
            enrollment__student__user=self.request.user
        ).values(
            'dept', 'course_number', 'professor', 'pk', 'domain', 'name', 'enrollment__student__user__username',
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
            ).order_by('-join_date')[:5])
            from collections import namedtuple
            Activity = namedtuple('Activity', ['type', 'title', 'time', 'user'])

            # make the list unique
            latest_joins = list(set(latest_joins))

            joins = []
            for join in latest_joins:
                joins.append(Activity('join', join.student.name, join.join_date, join.student))

            both = list(random_mix(act, joins))
            course['activity'] = both
            students = Course.objects.get_classlist_for(Course.objects.get(pk=course['pk']))
            course['students'] = students

        data['course_list'] = courses

        return render(request, self.template_name, data)

    @method_decorator(class_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(ClassesView, self).dispatch(*args, **kwargs)

classes = ClassesView.as_view()

'''
url: /school/course/unsubscribe/
name: course_email_unsubscribe
'''
class EmailUnsubscribeView(View):
    def post(self, request, *args, **kwargs):
        pass

course_email_unsubscribe = EmailUnsubscribeView.as_view()

'''
url: /course/events/
'''
class CourseEventsView(View, AjaxableResponseMixin):

    def post(self, request, *args, **kwargs):
        return redirect(reverse('dashboard'))

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            course_id = request.GET.get('course_id', None)
            if not course_id:
                return self.render_to_json_response({}, status=400)

            query = request.GET.get('query', '')
            events = CalendarEvent.objects.filter(calendar__course__id=course_id, calendar__primary=True, title__icontains=query).values('id', 'title')
            data = dict(events=list(events))
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('dashboard'))

course_events = CourseEventsView.as_view()
