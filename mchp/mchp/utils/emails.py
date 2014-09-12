#!/usr/bin/env python3
import requests
import csv
from bs4 import BeautifulSoup

def get_email(first_name, last_name):
    base_url = 'http://directory.arizona.edu/phonebook?first_name={}&last_name={}&fac_staff_stud=2'
    url = base_url.format(first_name, last_name)
    res = requests.get(url)
    soup = BeautifulSoup(res.content)
    links = soup.findAll('a')
    matches = []
    for link in links:
        href = link.get('href')
        if 'mailto:' in href:
            matches.append((first_name, link.text, last_name))
    if not matches:
        print('not found for: '+first_name+last_name)
    return matches

email_list = []
with open('names.csv', newline='') as csvfile:
    name_reader = csv.reader(csvfile, delimiter=',', quotechar='\\')
    for row in name_reader:
        email_t = get_email(row[0], row[1].split(' ')[0])
        email_list.append(email_t)

with open('emails.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='\\')
    for emails in email_list:
        for email in emails:
            writer.writerow(email)

