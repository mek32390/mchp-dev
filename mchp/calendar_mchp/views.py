from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect#, get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, DeleteView,View
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
class CalendarCreateView(FormView, AjaxableResponseMixin):
    template_name = 'calendar_mchp/calendar_create.html'
    model = ClassCalendar

    def get(self, request, *args, **kwargs):
        data = {

        }
        return render(request, self.template_name, data)

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
url: /calendar/events/add
name: event_add
'''
class EventAddView(FormView, AjaxableResponseMixin):
    template_name = 'calendar_mchp/event_add.html'
    model = ClassCalendar

    def post(self, request, *args, **kwargs):
        start = timezone.make_aware(datetime.strptime(request.POST['start'], DATE_FORMAT),
                                  timezone.get_current_timezone())
        end = timezone.make_aware(datetime.strptime(request.POST['end'], DATE_FORMAT),
                                  timezone.get_current_timezone())
        all_day = request.POST.get('all_day', True)
        
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
            return self.render_to_json_response({}, status=200)
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
            events = list(CalendarEvent.objects.all().values('id', 'title', 'start', 'end',
                                                             'all_day'))
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
