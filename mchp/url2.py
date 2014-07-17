#!/usr/bin/env python2
from boto.s3.connection import S3Connection

import os
import sys

def url(key):
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'mchp-dev')
    connection = S3Connection( aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    url = connection.generate_url(200, 'GET', AWS_STORAGE_BUCKET_NAME, key,
        response_headers={ 'response-content-type': 'application/octet-stream' })
    return url

if __name__ == '__main__':
    print(url(sys.argv[1]))
