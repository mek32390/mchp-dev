from django.db import IntegrityError

class TimeOrderError(IntegrityError):
    pass

class CalendarExpiredError(IntegrityError):
    pass
