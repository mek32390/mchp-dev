from django.contrib import messages
from django.core.cache import get_cache
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models import Q, Count
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View

from lib.decorators import class_required
from schedule.models import SchoolQuicklink, SchoolAlias, Course
from calendar_mchp.models import CalendarEvent, ClassCalendar, Subscription
from dashboard.models import RSSSetting, Weather, DashEvent, RSSType, RSSLink
from dashboard.utils import DASH_EVENTS
from referral.models import ReferralCode

from datetime import timedelta
import pywapi
import json
import requests
import random

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ" 

'''
url: /home/
name: dashboard
'''
class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        s_links = SchoolQuicklink.objects.filter(
            domain=self.student.school
        ).order_by('id')

        events = CalendarEvent.objects.filter(
            Q(calendar__in=ClassCalendar.objects.filter(subscription__student=self.student,private=False))
            | Q(calendar__in=ClassCalendar.objects.filter(owner=self.student)),
            start__range=(timezone.now(), timezone.now() + timedelta(days=1))
        ).order_by('start')
        rss_types = RSSType.objects.filter(
            Q(school=self.student.school)
            |Q(school=None),
        )
        for rss in rss_types:
            links = RSSLink.objects.filter(
                rss_type=rss
            )
            setattr(rss, 'links', links)
        rss_settings = RSSSetting.objects.filter(
            student=self.student
        )
        show_rss = list(map(lambda setting: setting.rss_type, rss_settings))

        # filter all rss types w/ just the ones the user wants shown
        rss_types = [(rss,True) if rss in show_rss else (rss,False) for rss in rss_types]
        ref = ReferralCode.objects.get_referral_code(request.user)

        # school 
        school = self.student.school
        alias = SchoolAlias.objects.filter(
            domain=school
        )
        if alias.exists():
            setattr(school, 'alias', alias[0].alias)
        else:
            setattr(school, 'alias', school.name)

        # weather
        # the weather must be stored for 30 minutes before making another request i think this is a
        # license thing
        saved_weather = Weather.objects.filter(
            zipcode=school.zipcode,
            fetch__gte=timezone.now() + timedelta(minutes=-30),
        )
        if saved_weather.exists():
            weather = saved_weather[0]
            weather = weather.info if weather.info else None
        elif school.zipcode:
            saved_weather, created = Weather.objects.get_or_create(zipcode=school.zipcode)
            weather_info = pywapi.get_weather_from_weather_com(school.zipcode, units='imperial')
            weather_info = weather_info['current_conditions']
            weather = weather_info

            saved_weather.info = json.dumps(weather_info)
            saved_weather.save()
        else: 
            weather = None

        date_format = "%Y-%m-%dT%H:%M:%S%z" 
        time = timezone.localtime(timezone.now(),
                                  timezone.get_current_timezone()).strftime(date_format)

        classmates = Course.objects.get_classmates_for(self.student)
        # get rid of duplicates 
        classmates = list(set(classmates))
        sample_size = 2 if len(classmates) > 1 else len(classmates)
        classmates = random.sample(classmates, sample_size)
        for classmate in classmates:
            classes_in_common = Course.objects.get_classes_in_common(classmate, self.student)
            setattr(classmate, 'classes_in_common', classes_in_common)

        # check if they have cals or subscriptions
        events_possible = ClassCalendar.objects.filter(
            owner=self.student,
        ).exists() or Subscription.objects.filter(
            student=self.student,
        ).exists()

        dashboard_ref_flag = 'dashboard referral'
        data = {
            'dashboard_ref_flag': self.student.one_time_flag.get_flag(self.student, dashboard_ref_flag),
            'dashboard_ref_flag_name': dashboard_ref_flag, 
            'referral_info': ref,
            'school_links': s_links,
            'events': events[:5],
            'event_count': events.count(),
            'events_possible': events_possible,
            'rss_types': rss_types,
            'school': school,
            'weather': weather,
            'current_time': time,
            'classmates': classmates,
            'calendars': self._get_calendars(self.student.courses()),
            'referral_reward': settings.MCHP_PRICING['referral_reward']
        }
        return render(request, self.template_name, data)

    def _get_calendars(self, courses):
        subs = Subscription.objects.filter(
            student = self.student
        )
        if subs.exists():
            return []
        all_cals = []
        for course in courses:
            cals = ClassCalendar.objects.filter(
                course = course,
            ).annotate(
                subscriptions=Count('subscribers')
            ).order_by('subscriptions')
            all_cals = all_cals + list(cals)[:2]
        random.shuffle(all_cals)
        return all_cals[:4]

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    @method_decorator(ensure_csrf_cookie)
    @method_decorator(class_required)
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
url: /home/feed/
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
                                      'calendar__title', 'calendar__pk',
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

    @method_decorator(class_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(DashboardFeed, self).dispatch(*args, **kwargs)

feed = DashboardFeed.as_view()

'''
url: /home/rss-proxy/
name: dashboard_rss_proxy
'''
class DashboardRssProxy(View, AjaxableResponseMixin):

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            url = request.GET.get('url', None)
            if url == '' or not url:
                return HttpResponse({}, status=400)

            link = RSSLink.objects.filter(
                url=url
            )
            if link.exists():
                # each rss feed gets cached 
                cache_key = link[0].pk
            else:
                # only send requests to approved sites, otherwise any arbitrary url could be
                # requested by the user
                return HttpResponse({}, status=400)

            # try to return the page from cache so we don't slam rss feeds and get refused
            rss_cache = get_cache('rss_cache')
            rss_data = rss_cache.get(cache_key)

            # it was found in the cache
            if not rss_data == None:
                return HttpResponse(rss_data, status=200)

            # it hasn't been saved or it expired
            try:
                response = requests.get(url)
            except requests.exceptions.ConnectionError:
                return HttpResponse({'error': 'connection refused from ' + url}, status=400)
            # save it in the cache for 5 mins
            rss_lifetime = 300
            rss_cache.set(cache_key, response.content, rss_lifetime)
            # return the rss data
            return HttpResponse(response.content, status=200)
        else:
            return redirect(reverse('dashboard'))

    @method_decorator(class_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(DashboardRssProxy, self).dispatch(*args, **kwargs)

rss_proxy = DashboardRssProxy.as_view()


'''
url: /home/toggle-rss/
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
