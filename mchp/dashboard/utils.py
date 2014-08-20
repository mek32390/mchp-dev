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

DASH_EVENT_LIST = [
    'calendar purchase',
    'calendar add',
    'document purchase',
    'document add',
    'other class join',
    'class join',
]
DASH_EVENT_LIST = list(zip(range(100), DASH_EVENT_LIST))

WEATHER_ICONS = {
    32: 'wi wi-day-sunny'
}
