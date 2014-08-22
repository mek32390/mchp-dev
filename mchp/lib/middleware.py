import pytz

from django.utils import timezone
from django.contrib import messages

class TimezoneMiddleware(object):
    # activate the current time zone for the student according to their school time zone
    def process_request(self, request):
        if not request.user.is_anonymous() and request.user.student_exists():
            tz = request.user.student.school.timezone
            if tz:
                timezone.activate(pytz.timezone(tz))
            else:
                timezone.deactivate()

class CustomMessageMiddleware(object):

    def process_request(self, request):
        storage = messages.get_messages(request)
        mes = []
        # what = storage.inbox_list(request.user)
        for message in storage:
            mes.append(message)
        setattr(request, 'rails_messages', mes)
        # storage.used = False
