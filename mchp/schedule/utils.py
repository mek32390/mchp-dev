import re
from django.core.exceptions import ValidationError
import schedule.models

def clean_domain(value):
    edu = re.compile('.*(\.edu/?)$')
    if not re.match(edu, value):
        raise ValidationError('School domain did not end in .edu: {}'.format(value))

from faker import Faker
from faker.providers import BaseProvider
from random import randrange,choice

fake_course = Faker()

# create new provider class
class ClassProvider(BaseProvider):
    def dept(self):
        length = 3 if randrange(10) % 2 == 0 else 4
        dept = ''
        for _ in range(length):
            letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            dept += choice(letters)
        return dept

    def course_number(self):
        return randrange(100, 999)

    def professor(self):
        return fake_course.first_name()

    def course(self):
        return self.dept() + str(self.course_number()) + ' with instructor ' + self.professor()

fake_course.add_provider(ClassProvider)

def add_course_to_db(school, num, **kwargs):
    for _ in range(num):
        if 'dept' in kwargs:
            dept = kwargs['dept']
        else:
            dept = fake_course.dept()
        course = schedule.models.Course(
            domain=school, 
            dept=dept,
            course_number=fake_course.course_number(),
            professor=fake_course.professor(),
        )
        course.save()

def fill_schools():
    import csv
    with open('./schedule/Schools.csv', newline='') as csvfile:
        school_reader = csv.reader(csvfile, delimiter=',', quotechar='\\')
        for row in school_reader:
            s = schedule.models.School(
                domain = row[0],
                name = row[1],
                phone_number = row[2],
                address = row[3],
                city = row[4],
                state = row[5],
                country = row[6],
            )
            s.save()

US_STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
# Territories
    ('AS', 'American Samoa'),
    ('GU', 'Guam'),
    ('MP', 'Northern Mariana Islands'),
    ('PR', 'Puerto Rico'),
    ('VI', 'Virgin Islands'),
)
