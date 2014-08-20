RSS_ICONS = [
    ('Breaking', 'fa-header'), 
    ('Score', 'fa-dribbble'), 
    ('Campus Life', 'fa-paper-plane-o'), 
    ('Viral', 'fa-globe'), 
    ('Tech', 'fa-code'), 
    ('Corporate', 'fa-usd'), 
    ('Hollywood', 'fa-ticket'), 
    ('Fresh Eats', 'fa-leaf'),  
]
RSS = [rss[0] for rss in RSS_ICONS]
RSS_LIST = list(zip(range(100), RSS))

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
    # text: rain
    12: 'wi wi-rain',
    # partly cloudy
    29: 'wi wi-night-cloudy',
    # text: clear
    31: 'wi wi-night-clear',
    # text: clear
    32: 'wi wi-day-sunny',
}
