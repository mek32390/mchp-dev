import re
from django.core.exceptions import ValidationError

def clean_domain(value):
    edu = re.compile('.*(\.edu/?)$')
    if not re.match(edu, value):
        raise ValidationError('School domain did not end in .edu: {}'.format(value))
