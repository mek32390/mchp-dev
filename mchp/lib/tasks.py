from __future__ import absolute_import

from celery.utils.log import get_task_logger

import uwsgi
from uwsgidecorators import timer

import requests

logger = get_task_logger(__name__)

@timer(10)
def ping_site():
    url = 'https://www.mycollegehomepage.com'

    try:
        r = requests.get(url, verify=False, timeout=10)
        if r.status_code != 200:
            raise
    except:
        uwsgi.reload()

