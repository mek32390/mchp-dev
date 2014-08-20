from django.dispatch import Signal

calendar_event_created = Signal(providing_args=['event'])
