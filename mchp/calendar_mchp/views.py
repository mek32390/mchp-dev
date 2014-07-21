from allauth.account.decorators import verified_email_required

from django.contrib import messages
# from django.conf import settings
# from django.core import serializers
# from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render #get_object_or_404, redirect
# from django.template import Context
# from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, DeleteView,View
# from django.views.generic.list import ListView

from calendar_mchp.models import ClassCalendar

import json
import logging
logger = logging.getLogger(__name__)

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

    @method_decorator(verified_email_required)
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
class EventAddView(FormView):
    template_name = 'calendar_mchp/event_add.html'
    model = ClassCalendar

    def get(self, request, *args, **kwargs):
        data = {

        }
        return render(request, self.template_name, data)
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

    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        self.student = self.request.user.student
        return super(CalendarView, self).dispatch(*args, **kwargs)

calendar = CalendarView.as_view()
