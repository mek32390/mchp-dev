from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic.edit import View

from lib.decorators import school_required
from notification.api import mark_all_read

import json

'''
url: /mark-all/
name: mark_all_notifications
'''
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

class MarkAllNotificationsView(View, AjaxableResponseMixin):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            mark_all_read(request.user)
            data = {
            }
            return self.render_to_json_response(data)
        else:
            return redirect(reverse('my_profile'))

    @method_decorator(school_required)
    def dispatch(self, *args, **kwargs):
        return super(MarkAllNotificationsView, self).dispatch(*args, **kwargs)

mark_all_notifications = MarkAllNotificationsView.as_view()
