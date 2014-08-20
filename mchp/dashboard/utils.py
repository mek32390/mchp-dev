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
    # t-storms late
    4: 'wi wi-storm-showers',

    # n/d showers 
    11: 'wi wi-showers',

    # n/d: rain
    12: 'wi wi-rain',

    # n/d: drifting snow / windy
    15: 'wi wi-snow-wind',

    # m: waning crescent
    #24: 'wi wi-moon-waning-crescent',

    # d: partly cloudy / windy
    24: 'wi wi-cloudy-windy',

    # moon: waning crescent
    25: 'wi wi-moon-waning-crescent',

    # n: mostly cloudy
    27: 'wi wi-cloudy',

    # d: mostly cloudy
    28: 'wi wi-cloudy',

    # n: partly cloudy
    29: 'wi wi-night-cloudy',

    # d: partly couldy
    30: 'wi wi-cloudy',

    # n: clear
    31: 'wi wi-night-clear',

    # d: sunny
    32: 'wi wi-day-sunny',

    # n: mostly clear / fair
    33: 'wi wi-cloud',

    # d: mostly sunny / fair
    34: 'wi wi-day-sunny',

    # d: scattered T-storms
    38: 'wi wi-storm-showers',

    # d: AM showers
    39: 'wi wi-day-showers',

    # # n: showers late
    # 45: 'wi wi-night-alt-showers',

    # # d: showers early
    # 45: 'wi wi-day-showers',

    # n: snow-showers 
    46: 'wi wi-rain-mix',

    # # d: t-storms early
    # 47: 'wi wi-day-thunderstorm',

    # n: scattered t-storms 
    47: 'wi wi-thunderstorm',


}
