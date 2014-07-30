from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect#, get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,View, UpdateView
# from django.views.generic.list import ListView

from calendar_mchp.models import ClassCalendar, CalendarEvent
from lib.decorators import school_required

from datetime import datetime
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

'''
url: /calendar/create/
name: calendar_create
'''
class CalendarCreateView(View, AjaxableResponseMixin):
    template_name = 'calendar_mchp/calendar_create.html'

    def get_success_url(self):
        return reverse('calendar')

    def get(self, request, *args, **kwargs):
        courses = self.student.courses.all()
        data = {
            'courses': courses,
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        # were just going to forgo any fancy django form saving for this one
        # cal_type = request.POST.get('cal-type', '')
        print(request.POST)
        return redirect(reverse('calendar_create'))
        return redirect(self.get_success_url())

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

calendar_delete = CalendarDeleteView.as_view()

'''
url: /calendar/events/add/
name: event_add
'''
class EventAddView(View, AjaxableResponseMixin):
    template_name = 'calendar_mchp/event_add.html'
    model = CalendarEvent

    def post(self, request, *args, **kwargs):
        # convert Full Calendar time strings to datetime objects, with timezones
        start = timezone.make_aware(datetime.strptime(request.POST['start'], DATE_FORMAT),
                                  timezone.get_current_timezone())
        end = timezone.make_aware(datetime.strptime(request.POST['end'], DATE_FORMAT),
                                  timezone.get_current_timezone())
        all_day = request.POST.get('all_day', True)
        
        # add the event
        calendar = ClassCalendar.objects.default(self.student)
        event_data = {
            'calendar': calendar,
            'title': request.POST['title'],
            'start': start,
            'end': end,
            'all_day': all_day
        }
        event = CalendarEvent(**event_data)
        event.save()
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
        data = {
            'flags': self.student.one_time_flag.default(self.student)
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
                calendar__owner=self.student
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
