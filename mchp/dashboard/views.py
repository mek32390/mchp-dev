from django.http import HttpResponseNotAllowed
from django.db.models import Q
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View

from lib.decorators import school_required
from lib import utils
from schedule.models import Course, SchoolQuicklink
from user_profile.models import Enrollment
from documents.models import Document
from calendar_mchp.models import CalendarEvent, ClassCalendar

from datetime import timedelta

class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        student_classes = Course.objects.filter(
            student=self.student
        )
        latest_joins = []

        # get some of the latest people to join your classes
        latest_joins = list(Enrollment.objects.filter(
            course__in=student_classes
        ).exclude(
            student=self.student
        ).order_by('join_date')[:5])
        from collections import namedtuple
        Activity = namedtuple('Activity', ['type', 'title', 'time', 'user'])

        # make the list unique
        latest_joins = list(set(latest_joins))
        
        docs = []
        for course in student_classes:
            docs += Document.objects.recent_events(course)

        joins = []
        for join in latest_joins:
            joins.append(Activity('join', join.student.name, join.join_date, ''))

        joins = list(set(joins))
        both = list(utils.random_mix(docs, joins))

        s_links = SchoolQuicklink.objects.filter(
            domain=self.student.school
        )

        events = CalendarEvent.objects.filter(
            Q(calendar__in=ClassCalendar.objects.filter(subscription__student=self.student))
            | Q(calendar__in=ClassCalendar.objects.filter(owner=self.student)),
            start__range=(timezone.now(), timezone.now() + timedelta(days=1))
        )
        data = {
            'flags': self.student.one_time_flag.default(self.student),
            'pulse': both,
            'school_links': s_links,
            'events': events[:5],
            'event_count': events.count(),
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    @method_decorator(ensure_csrf_cookie)
    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(DashboardView, self).dispatch(*args, **kwargs)

dashboard = DashboardView.as_view()
