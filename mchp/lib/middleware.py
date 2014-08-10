import pytz

from django.utils import timezone

class TimezoneMiddleware(object):
    # activate the current time zone for the student according to their school time zone
    def process_request(self, request):
        if not request.user.is_anonymous():
            tz = request.user.student.school.timezone
            if tz:
                timezone.activate(pytz.timezone(tz))
            else:
                timezone.deactivate()
