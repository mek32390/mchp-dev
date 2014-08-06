from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View

from lib.decorators import school_required
from lib import utils
from schedule.models import Course, SchoolQuicklink
from user_profile.models import Enrollment
from documents.models import Document

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
        print(s_links)
        data = {
            'flags': self.student.one_time_flag.default(self.student),
            'pulse': both,
            'school_links': s_links,
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
