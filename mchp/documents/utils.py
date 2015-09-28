from django.db import connection, connections
from django.core.files import File
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

import requests
import os
import uuid

from documents.models import Document
from documents.exceptions import DuplicateFileError

import datetime
from django.core.serializers.json import DjangoJSONEncoder
import decimal
from django.utils.timezone import is_aware


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def reupload_doc():
    cursor = connection.cursor()
    cursor.execute("select * from old_doc order by id")
    docs = dictfetchall(cursor)

    base_url = 'https://mchpstore.s3.amazonaws.com/'
    all_docs = []
    for doc in docs:
        old_id = doc['id']
        cursor.execute('select id from documents_document where old_id = %s and preview = \'\'', [old_id])
        document = cursor.fetchone()
        if document:
            new_id = document[0]
            document = Document.objects.filter(
                id = new_id,
            )[0]
        else: 
            continue
        print(document.title)
        all_docs.append(document)
        continue
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
        new_file = File(f)
        document.document = new_file
        print('found ' + document.title)
        document.save()
    return all_docs

def fix_thumbs():
    docs = Document.objects.all()
    from wand.image import Image
    from django.core.files.images import ImageFile
    for doc in docs:
        preview = doc.preview
        img = Image(filename=doc.preview.url)
        if img.height > 600:
            img.crop(0,0,500,600)
            preview_name = '/tmp/fuck'
            img.save(filename=preview_name)
            doc.preview.delete()
            doc.preview.save(preview.name, ImageFile(open(preview_name, 'rb'), preview_name))
            os.remove(preview_name)
            print(preview.name)

def upload_doc():
    cursor = connection.cursor()
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

class DjangoOverrideJSONEncoder(DjangoJSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time and decimal types.
    """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            df = DateFormat(o)
            r = df.format(get_format('DATE_FORMAT'))
            return r
        elif isinstance(o, datetime.date):
            df = DateFormat(o)
            r = df.format(get_format('DATE_FORMAT'))
            return r
        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            df = DateFormat(o)
            r = df.format(get_format('DATE_FORMAT'))
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return super(DjangoOverrideJSONEncoder, self).default(o)