from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect
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
from dashboard.models import RSSSetting, Weather
from dashboard.utils import RSS_ICONS
from referral.models import ReferralCode

from datetime import timedelta
import pywapi
import json

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
        ).order_by('start')
        rss_types = list(zip(range(100), RSS_ICONS))
        show_rss = list(map(lambda setting: setting.rss_type, RSSSetting.objects.filter(
            student=self.student
        )))
        # filter all rss types w/ just the ones the user wants shown
        rss_types = [(rss,icon,True) if rss in show_rss else (rss,icon,False) for rss,icon in rss_types]
        ref = ReferralCode.objects.get_referral_code(request.user)

        # school 
        school = self.student.school
        # weather
        # the weather must be stored for 30 minutes before making another request i think this is a
        # license thing
        saved_weather = Weather.objects.filter(
            zipcode=school.zip_code,
            fetch__gte=timezone.now() + timedelta(minutes=-30),
        )
        if saved_weather.exists():
            weather = saved_weather[0].info
        else:
            saved_weather, created = Weather.objects.get_or_create(zipcode=school.zip_code)
            weather_info = pywapi.get_weather_from_weather_com(school.zip_code, units='imperial')
            weather_info = weather_info['current_conditions']
            weather = weather_info

            saved_weather.info = json.dumps(weather_info)
            saved_weather.save()

        data = {
            'dashboard_ref_flag': self.student.one_time_flag.get_flag(self.student, 'dashboard ref'),
            'referral_info': ref,
            'pulse': both,
            'school_links': s_links,
            'events': events[:5],
            'event_count': events.count(),
            'rss_types': rss_types,
            'school': school,
            'weather': weather,
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

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.

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

    def send_ajax_error_message(self, message, **kwargs):
        messages.error(
            self.request,
            message,
        )
        data = {
            'messages': self.ajax_messages(),
        }
        status = kwargs.get('status', 500)
        return self.render_to_json_response(data, status=status)

'''
url: /dashboard/toggle-rss/
name: toggle_rss
'''
class ToggleRSSSetting(View, AjaxableResponseMixin):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            setting = request.POST.get('setting', None)
            if setting != None:
                RSSSetting.objects.toggle_setting(request.user.student, setting)
                return self.render_to_json_response({}, status=200)
            else:
                return self.render_to_json_response({}, status=403)
        else:
            return redirect(reverse('dashboard'))

    def get(self, request, *args, **kwargs):
        return redirect(reverse('dashboard'))

toggle_rss = ToggleRSSSetting.as_view()
