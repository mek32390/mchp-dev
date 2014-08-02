from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect#, get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,View, UpdateView
# from django.views.generic.list import ListView

from calendar_mchp.models import ClassCalendar, CalendarEvent, CourseDay
from calendar_mchp.exceptions import TimeOrderError
from lib.decorators import school_required
from schedule.models import Course
from schedule.utils import WEEK_DAYS

from datetime import datetime,timedelta
import json
import logging
logger = logging.getLogger(__name__)

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ" 

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
url: /calendar/create/
name: calendar_create
'''
class CalendarCreateView(View, AjaxableResponseMixin):
    template_name = 'calendar_mchp/calendar_create.html'

    def get_success_url(self):
        return reverse('calendar')

    def get(self, request, *args, **kwargs):
        courses = self.student.courses.exclude(
            id__in = self.student.calendars.all().values('course__pk')
        )
        data = {
            'courses': courses,
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return redirect(reverse('calendar'))
        # were just going to forgo any fancy django form saving for this one
        cal_type = request.POST.get('cal-type', '')

        if cal_type.lower() == 'class':
            # this is a sellable calendar
            calendar = self._make_calendar(request)
            try:
                calendar.save()
            except (IntegrityError, TimeOrderError) as err:
                # they made a calendar for this class
                if err.__class__ == IntegrityError:
                    return self.send_ajax_error_message('You have already made a calendar for that course', status=403)
                else:
                    # the start date was too early
                    return self.send_ajax_error_message(str(err), status=403)
            # now add the times as recurring events
            return self._make_times(request.POST.get('times', {}), calendar)
            # succes in submitting form
            return self.render_to_json_response({}, status=200)
        elif cal_type.lower() == 'personal':
            # this is a personal calendar, which we don't have yet
            return self.send_ajax_error_message("We don't do those yet.", status=501)
        else: 
            # this wasn't anything
            return self.send_ajax_error_message("Im not sure what calendar you wanted", status=403)

        return redirect(reverse('calendar_create'))

    def _make_calendar(self, request):
        course = Course.objects.filter(
            pk=request.POST.get('course', ''),
            student=self.student,
        )
        if not course.exists():
            # you can only create a calendar for a course you're enrolled in
            return self.send_ajax_error_message('You are not enrolled in that class', status=403)
        else:
            # course found
            course = course[0]

        end_date = timezone.make_aware(datetime.strptime(
            request.POST.get('enddate', ''), "%m/%d/%Y"),
            timezone.utc)
        calendar_data = {
            'course': course,
            'owner': self.student,
            'description': request.POST.get('description', ''),
            'end_date': end_date,
            'private': request.POST.get('private', True),
        }
        return ClassCalendar(**calendar_data)
    
    def _make_times(self, times, calendar):
        times = json.loads(times)
        for day in times:
            event_data = {
                'calendar': calendar,
                'title': 'hold',
                'all_day': False,
                'is_recurring': True,
            }
            event = CalendarEvent(**event_data)
            # TODO error handling
            event.save()

            start_time = timezone.make_aware(datetime.strptime(
                times[day]['start'], DATE_FORMAT),
                timezone.utc)
            end_time = timezone.make_aware(datetime.strptime(
                times[day]['end'], DATE_FORMAT),
                timezone.utc)
            course_day_data = {
                'calendar': calendar,
                'event': event,

                'day': WEEK_DAYS.index(day),
                'start_time': start_time,
                'end_time': end_time,
            }
            course_day = CourseDay(**course_day_data)
            # TODO error handling
            course_day.save()

        return self.render_to_json_response({}, status=200)

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarCreateView, self).dispatch(*args, **kwargs)

calendar_create = CalendarCreateView.as_view()

'''
url: /calendar/delete/
name: calendar_delete
'''
class CalendarDeleteView(DeleteView, AjaxableResponseMixin):
    model = ClassCalendar

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            print(request.POST)
            cal = ClassCalendar.objects.filter(
                owner=self.student,
                pk = request.POST.get('id', None)
            )
            if cal.exists():
                cal = cal[0]
                cal.delete()

                messages.success(
                    self.request,
                    "Calendar deleted"
                )
                status = 200
            else:
                messages.error(
                    self.request,
                    "Is that really your calendar?"
                )
                status = 403
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data, status=status)
        else:
            return redirect(reverse('calendar'))

    def get(self, request, *args, **kwargs):
        return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarDeleteView, self).dispatch(*args, **kwargs)

calendar_delete = CalendarDeleteView.as_view()

'''
url: /calendar/events/add/
name: event_add
'''
class EventAddView(View, AjaxableResponseMixin):
    template_name = 'calendar_mchp/event_add.html'
    model = CalendarEvent

    def post(self, request, *args, **kwargs):
        print(request.POST)
        # convert Full Calendar time strings to datetime objects, with timezones
        date = request.POST.get('date', '1970-1-1')
        date_format = '%Y-%m-%d'

        start = timezone.make_aware(
            datetime.strptime(date, date_format),
            timezone.utc)
        end = start + timedelta(hours=1)

        # the calendar this event belongs to
        # TODO errors...
        calendar = ClassCalendar.objects.filter(
            pk=request.POST['calendar'],
            owner=self.student
        )[0]

        due = request.POST.get('due', 1)
        # 3 == at midnight
        if due == 3:
            all_day = True 
            start_time = start 
            end_time = end
        else:
            # otherwise, try to match the time to class start
            all_day = False

            # the course
            course_day = CourseDay.objects.filter(
                calendar=calendar,
                day = start.weekday()
            )
            if course_day.exists():
                course_day = course_day[0]
                start_time = datetime.combine(start, course_day.start_time)
                start_time = timezone.make_aware(
                    start_time,
                    timezone.utc
                )
                end_time = datetime.combine(start, course_day.end_time)
                end_time = timezone.make_aware(
                    end_time,
                    timezone.utc
                )
            else:
                start_time = start 
                end_time = end

        # add the event

        event_data = {
            'calendar': calendar,
            'title': request.POST['title'],
            'description': request.POST['description'],
            'start': start_time,
            'end': end_time,
            'all_day': all_day
        }
        event = CalendarEvent(**event_data)
        event.save()
        print(event)
        if self.request.is_ajax():
            messages.success(
                self.request,
                "Event added"
            )
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('calendar'))

    def get(self, request, *args, **kwargs):
        data = {

        }
        return render(request, self.template_name, data)

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(EventAddView, self).dispatch(*args, **kwargs)

event_add = EventAddView.as_view()

'''
url: /calendar/events/update/
name: event_update
'''
class EventUpdateView(UpdateView, AjaxableResponseMixin):
    model = CalendarEvent

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            event = CalendarEvent.objects.filter(
                calendar__owner=self.student,
                id = request.POST.get('id', None)
            )
            if event.exists():
                event = event[0]
                start = timezone.make_aware(datetime.strptime(request.POST['start'], DATE_FORMAT),
                                            timezone.get_current_timezone())
                end = timezone.make_aware(datetime.strptime(request.POST['end'], DATE_FORMAT),
                                          timezone.get_current_timezone())
                all_day = request.POST.get('all_day', True)
                event.start = start
                event.end = end
                event.all_day = all_day
                event.save()

                messages.success(
                    self.request,
                    "Event updated"
                )
            else:
                messages.error(
                    self.request,
                    "Event not found"
                )
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('calendar'))

    def get(self, request, *args, **kwargs):
        return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(EventUpdateView, self).dispatch(*args, **kwargs)

event_update = EventUpdateView.as_view()

'''
url: /calendar/events/delete/
name: event_delete
'''
class EventDeleteView(DeleteView, AjaxableResponseMixin):
    model = CalendarEvent

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            event = CalendarEvent.objects.filter(
                calendar__owner=self.student,
                id = request.POST.get('id', None)
            )
            if event.exists():
                event = event[0]
                event.delete()

                messages.success(
                    self.request,
                    "Event deleted"
                )
            else:
                messages.error(
                    self.request,
                    "Event not found"
                )
            data = {
                'messages': self.ajax_messages(),
            }
            return self.render_to_json_response(data, status=200)
        else:
            return redirect(reverse('calendar'))

    def get(self, request, *args, **kwargs):
        return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(EventDeleteView, self).dispatch(*args, **kwargs)

event_delete = EventDeleteView.as_view()

'''
url: /calendar/preview/<uuid>
name: calendar_preview
'''
class CalendarPreview(DetailView):
    template_name = 'calendar_mchp/calendar_preview.html'
    model = ClassCalendar

    def get(self, request, *args, **kwargs):
        data = {

        }
        return render(request, self.template_name, data)
calendar_preview = CalendarPreview.as_view()

'''
url: /calendar/
name: calendar
'''
class CalendarView(View):
    template_name = 'calendar_mchp/calendar.html'

    def get(self, request, *args, **kwargs):
        owned_calendars = ClassCalendar.objects.filter(
            owner=self.student
        )
        data = {
            'flags': self.student.one_time_flag.default(self.student),
            'owned_calendars': owned_calendars,
        }
        return render(request, self.template_name, data)

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarView, self).dispatch(*args, **kwargs)

calendar = CalendarView.as_view()

'''
url: /calendar/feed/
name: calendar_feed
'''
class CalendarFeed(View, AjaxableResponseMixin):

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            events = list(CalendarEvent.objects.filter(
                calendar__owner=self.student,
                is_recurring=False,
            ).values('id', 'title', 'start', 'end', 'all_day', 'url'))
            # convert the returned events to a format fullcalendar understands
            for event in events:
                event['start'] = event['start'].strftime(DATE_FORMAT)
                event['end'] = event['end'].strftime(DATE_FORMAT)
                event['allDay'] = event['all_day']
                del event['all_day']
            return self.render_to_json_response(events, status=200)
        else:
            return redirect(reverse('calendar'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarFeed, self).dispatch(*args, **kwargs)

calendar_feed = CalendarFeed.as_view()
