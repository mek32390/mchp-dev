from django.db import connection, connections
from django.core.files import File

import requests
import os
import uuid

from documents.models import Document
from documents.exceptions import DuplicateFileError

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def upload_doc():
    cursor = connections['production'].cursor()
    cursor.execute("select * from old_doc order by id")
    docs = dictfetchall(cursor)

    base_url = 'https://mchpstore.s3.amazonaws.com/'
    for doc in docs:
        url = base_url+"{}".format(doc['path'])

        r = requests.get(url, stream=True)
        doc_name = os.path.basename(doc['name'])
        filename = '/tmp/{}.pdf'.format(doc_name)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        f = open(filename, 'rb')
        document = File(f)

        cursor.execute('select id from schedule_course where old_id = %s', [doc['course']])
        try:
            course = cursor.fetchall()[0][0]
            print('{}. creating {}'.format(doc['id'], doc_name))
        except:
            print('{}. no course'.format(doc['id']))
            continue

        data = {
            'title': doc['name'],
            'description': doc['description'],
            'course_id': course,
            'price': doc['price'],
            'create_date': str(doc['created'])+'+00',
            'document': document,
        }
        new_doc = Document(**data)
        try:
            new_doc.save()
        except DuplicateFileError:
            print('{} has already been uploaded'.format(doc_name))

        f.close()
        cursor.execute('update documents_document set old_id = %s where id = %s', 
                       [doc['id'], new_doc.id]
                      )

        os.remove(filename)
