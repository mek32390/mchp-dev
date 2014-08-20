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
# from lib import utils
from schedule.models import SchoolQuicklink
# from user_profile.models import Enrollment
# from documents.models import Document
from calendar_mchp.models import CalendarEvent, ClassCalendar
from dashboard.models import RSSSetting, Weather, DashEvent, RSSType, RSSLink
from dashboard.utils import DASH_EVENTS
from referral.models import ReferralCode

from datetime import timedelta
import pywapi
import json
from random import randrange

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ" 

class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        s_links = SchoolQuicklink.objects.filter(
            domain=self.student.school
        )

        events = CalendarEvent.objects.filter(
            Q(calendar__in=ClassCalendar.objects.filter(subscription__student=self.student))
            | Q(calendar__in=ClassCalendar.objects.filter(owner=self.student)),
            start__range=(timezone.now(), timezone.now() + timedelta(days=1))
        ).order_by('start')
        rss_types = RSSType.objects.all()
        for rss in rss_types:
            links = RSSLink.objects.filter(
                rss_type=rss
            )
            setattr(rss, 'links', links)
        show_rss = list(map(lambda setting: setting.rss_type, RSSSetting.objects.filter(
            student=self.student
        )))

        # filter all rss types w/ just the ones the user wants shown
        rss_types = [(rss,True) if rss in show_rss else (rss,False) for rss in rss_types]
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

        date_format = "%Y-%m-%dT%H:%M:%S%z" 
        time = timezone.localtime(timezone.now(),
                                  timezone.get_current_timezone()).strftime(date_format)

        data = {
            'dashboard_ref_flag': self.student.one_time_flag.get_flag(self.student, 'dashboard ref'),
            'referral_info': ref,
            'school_links': s_links,
            'events': events[:5],
            'event_count': events.count(),
            'rss_types': rss_types,
            'school': school,
            'weather': weather,
            'current_time': time,
            'classmates': [self._get_classmate()],
        }
        return render(request, self.template_name, data)

    def _get_classmate(self):
        courses = self.student.courses.all()
        if not len(courses):
            return None
        course = courses[randrange(len(courses))]
        people = list(course.student_set.exclude(pk=self.student.pk))
        if people:
            person = people[randrange(len(people))]
        else: 
            return self._get_classmate()
        print(person)
        return person

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
url: /dashboard/feed/
name: dashboard_feed
'''
class DashboardFeed(View, AjaxableResponseMixin):

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            feed = DashEvent.objects.filter(
                followers__id__exact=self.student.id
            ).select_related().values('type', 'date_created', 
                                      'course__dept', 'course__course_number', 'course__pk',
                                      'document__title', 'document__uuid',
                                      'event__title', 
                                      'student__user__username', 'student__pk',
                                     ).order_by('-date_created')
            for item in feed:
                item['time'] = item['date_created'].strftime(DATE_FORMAT)
                del item['date_created']
                event_type = DASH_EVENTS[item['type']].replace(' ', '-')
                item['type'] = event_type

            data = {
                'feed': list(feed),
            }
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('dashboard'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(DashboardFeed, self).dispatch(*args, **kwargs)

feed = DashboardFeed.as_view()


'''
url: /dashboard/toggle-rss/
name: toggle_rss
'''
class ToggleRSSSetting(View, AjaxableResponseMixin):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            setting = RSSType.objects.filter(
                pk=request.POST.get('setting', None)
            )
            if setting.exists():
                RSSSetting.objects.toggle_setting(request.user.student, setting[0])
                return self.render_to_json_response({}, status=200)
            else:
                return self.render_to_json_response({}, status=403)
        else:
            return redirect(reverse('dashboard'))

    def get(self, request, *args, **kwargs):
        return redirect(reverse('dashboard'))

toggle_rss = ToggleRSSSetting.as_view()
