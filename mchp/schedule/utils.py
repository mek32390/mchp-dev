import re
from django.core.exceptions import ValidationError
import schedule.models

import requests
from bs4 import BeautifulSoup

def clean_domain(value):
    edu = re.compile('.*(\.edu/?)$')
    if not re.match(edu, value):
        raise ValidationError('School domain did not end in .edu: {}'.format(value))

def add_timezones():
    import os
    import json
    from time import sleep
    import time
    google_base_url = 'https://maps.googleapis.com/maps/api/'
    key = os.getenv('GOOGLE_API_KEY', '')
    index = 2586
    stop = 4000
    schools = schedule.models.School.objects.all().order_by('name')[index:stop]
    for school in schools:
        index = index+1
        if not school.zipcode:
            url = google_base_url + 'geocode/json'
            sleep(.3)
            print(str(index) + '. ' + school.name)
            address = school.address + " " + school.city + " " + school.state
            params = {
                'key': key,
                'address': address,
            }
            response = requests.get(url, params=params)
            info = json.loads(response.content.decode('utf-8'))
            if info['status'] != "OK":
                print(info['status'])
                continue
            else:
                results = info['results']
            for result in results:
                loc = result['geometry']['location']
                lat = loc['lat']
                lng = loc['lng']
                school.lat = lat
                school.lng = lng
                print(lat)
                print(lng)
                for component in result['address_components']:
                    if component['types'] and component['types'][0] == 'postal_code':
                        zipcode = component['long_name']
                        school.zipcode = zipcode
                        print(zipcode)
                print('\n')
            school.save()

        url = google_base_url + 'timezone/json'
        if not school.lat or school.timezone:
            continue
        sleep(.3)
        print(str(index) + '. ' + school.name)
        params = {
            'key': key,
            'location': str(school.lat) + "," + str(school.lng),
            'timestamp': int(time.time())
        }
        response = requests.get(url, params=params)
        info = json.loads(response.content.decode('utf-8'))
        if info['status'] != "OK":
            print(info['status'])
            continue
        else:
            school.timezone = info['timeZoneId']
            school.save()
            results = info['timeZoneId']
            print(results)

def scrape():
    schools = schedule.models.School.objects.all().order_by('name')[1349:]
    num = 1349
    for school in schools:
        num += 1
        print(str(num) + " " + str(school))
        url = "http://"+school.domain
        try:
            res = requests.get(url)
        except:
            continue
        soup = BeautifulSoup(res.content)
        links = soup.findAll('a')
        approve_list = []
        other = []
        for link in links:
            href = link.get('href')
            if not href:
                continue
            ban_list = ['youtube', 'facebook', 'flickr', 'login', 'twitter']
            if not href.startswith(('http://', 'https://')):
                continue;
            if any(word in href for word in ban_list):
                continue
            if "email" in href or "my" in href or "blackboard" in href or "d2l" in href or 'calendar' in href:
                approve_list.append(href)
            other.append(href)

        approve_list = list(set(approve_list))[:20]
        for link in approve_list:
            if len(link) > 200:
                continue
            from urllib.parse import urlparse
            parts = urlparse(link)
            name = parts.hostname.split('.')[1]
            path = parts.path.split('/')[-1]
            if path:
                name = path.split('.')[0]
            name = name[:40]
            ql = schedule.models.SchoolQuicklink(quick_link=link, name=name,
                                            domain=school
                                            )
            from django.db import IntegrityError
            try:
                ql.save()
            except IntegrityError:
                pass

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

def fill_majors():
    with open('./schedule/majors.txt') as file:
        for major in file:
            dept = schedule.models.Major(name=major.rstrip('\n'))
            dept.save()
            print(major.rstrip('\n'))

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

WEEK_DAYS = [
    'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat'
]
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
