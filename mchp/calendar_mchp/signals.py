from django.dispatch import Signal

calendar_event_created = Signal(providing_args=['event'])
calendar_event_edited = Signal(providing_args=['event'])
