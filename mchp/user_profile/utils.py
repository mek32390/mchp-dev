ONE_TIME_EVENTS = [
    'calendar turtorial',
    'dashboard ref',
    'preview',
    'events turtorial',
]

ONE_TIME_EVENTS = list(zip(range(1, 100), ONE_TIME_EVENTS))
ONE_TIME_EVENTS_DICT = dict([(t[1], t[0]) for t in ONE_TIME_EVENTS])
