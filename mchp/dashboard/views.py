from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View

from lib.decorators import school_required
from schedule.models import Course

class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        student_classes = Course.objects.filter(
            student=self.student
        )
        latest_joins = []
        # get some of the latest people to join your classes
        for cls in student_classes:
            latest_joins += list(cls.student_set.exclude(
                user=request.user
            ).order_by('enrollment__join_date')[:5])

        # make the list unique
        latest_joins = list(set(latest_joins))
        print(latest_joins)
        data = {
            'flags': self.student.one_time_flag.default(self.student),
            'pulse': latest_joins,
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
