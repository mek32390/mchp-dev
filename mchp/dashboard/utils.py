DASH_EVENTS = [
    'calendar purchase',
    'calendar add',
    'document purchase',
    'document add',
    'other class join',
    'class join',
]
DASH_EVENT_LIST = list(zip(range(100), DASH_EVENTS))

WEATHER_ICONS = {
    # t-storms
    4: 'wi',

    # showers 
    11: 'wi',

    # text: rain
    12: 'wi wi-rain',

    # partly cloudy
    29: 'wi wi-night-cloudy',

    # partly couldy
    30: 'wi',

    # text: clear
    31: 'wi wi-night-clear',

    # text: sunny
    32: 'wi wi-day-sunny',

    # fair 
    33: 'wi wi-night-clear',

    # mostly sunny
    34: 'wi',

    # scattered T-storms
    38: 'wi',

    # AM showers
    39: 'wi',

    # showers late
    45: 'wi',

    # t-storms early
    47: 'wi',

}
