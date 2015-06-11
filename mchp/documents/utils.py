from django.db import connection, connections
from django.contrib.auth.models import User
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


def parse_roster(html):
    """ Parse an HTML roster into a collection of users.

    Parameters
    ----------
    html : str
        HTML data to parse.

    Returns
    -------
    out : list of dict
        A collection of parsed items.

    """
    out = []
    # [TODO] flesh me out
    return out


def ensure_enrollment_exists(course, student, receive_email=True):
    """ Enroll a student if not already enrolled.

    Parameters
    ----------
    course : schedule.models.Course
        A course in which to enroll a student.
    student : user_profile.models.Student
        A student to enroll in a course.
    receive_email : bool, optional
        Should a new enrollee receive e-mail?  Default `True`.
        Has no effect if enrollment already exists.

    Returns
    -------
    out : schedule.models.Enrollment
        A new or existing enrollment record for a student in the given course.

    """
    from schedule.models import Enrollment
    enrollment, _ = Enrollment.objects.get_or_create(
        course=course,
        student=student,
        defaults={'receive_email': receive_email})
    return enrollment


def ensure_student_exists(school, user):
    """ Create a student if they don't already exist.

    Parameters
    ----------
    school : schedule.models.School
        A school at which to create a student.
    user : django.conf.settings.AUTH_USER_MODEL
        A user for which to create a student.

    Returns
    -------
    out : user_profile.models.Student
        A new or existing student.

    """
    from user_profile.models import Student
    student = user.student_user
    if not student:
        student = Student.objects.create_student(user, school)
    return student


def suffix(s, suffix, max_length):
    """ Take a string and replace the end with a suffix.

    Parameters
    ----------
    s : str
        A string to suffix.
    suffix : str
        A stuffix for the string.
    max_length : int
        The maximum allowed length of the string.

    Returns
    -------
    out : str
        The suffixed string.

    Raises
    ------
    ValueError
        If length of `suffix` exceeds `max_length`.

    Notes
    -----
    Some output examples:

        joe.q.public, '', 8 => joe.q.pu
        joe.q.public, 'jr', 8 => joe.q.jr
        joe.q.public, 'jr', 8 => joe.q.jr
        joe.q.public, '', 20 => joe.q.public
        joe.q.public, 'jr', 20 => joe.q.publicjr

    """
    suffix_len = len(suffix)
    if suffix_len > max_length:
        raise ValueError('Suffix length cannot exceed max length')
    return s[:max_length - suffix_len] + suffix


def incremental_suffixes(base, max_length, start=2):
    """ Generate successively-incremented numeric suffixes for a string.

    Parameters
    ----------
    base : str
        A base string.
    max_length : int
        The maximum allowed length of the string.
    start : int, optional
        The starting suffix.  Default `2` to signify a duplicate.

    Yields
    ------
    out : str
        The original string, constrained for length.
    out : str
        A suffixed and length-constrained string.

    Raises
    ------
    ValueError
        If length of number appended exceeds `max_length`.

    """
    from itertools import count
    yield suffix(base, '', max_length)
    for c in count(start):
        yield suffix(base, str(c), max_length)


def make_username(email):
    """ Generate a non-duplicate username.

    Parameters
    ----------
    email : str
        An e-mail address to process.

    Returns
    -------
    out : str
        The created username.

    """
    MAX_USERNAME_LENGTH = 30

    handle, _ = email.split('@')
    enumerator = incremental_suffixes(handle, MAX_USERNAME_LENGTH)
    while True:
        handle = next(enumerator)
        try:
            User.objects.get(username__iexact=handle)
        except User.DoesNotExist:
            break
    return handle


def ensure_user_exists(email, fname=None, lname=None):
    """ Find or create a user associated with a given e-mail address.

    Parameters
    ----------
    email : str
        An e-mail address associated with the user.
    fname : str, optional
        An optional first name for the user.
    lname : str, optional
        An optional last name for the user.

    Returns
    -------
    out : django.conf.settings.AUTH_USER_MODEL
        A new or existing user.

    Raises
    ------
    ValidationError
        If the given e-mail fails validation.

    Notes
    -----
    This searches not only the user model e-mail address, but also the
    addresses specified in the AllAuth inline.

    """
    from django.core.validators import validate_email
    from django.allauth.models import EmailAddress

    email = User.objects.normalize_email(email)
    validate_email(email)

    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        try:
            user = EmailAddress.objects.get(email__iexact=email).user
        except EmailAddress.DoesNotExist:
            username = make_username(email)
            params = {}
            if fname:
                params['first_name'] = fname
            if lname:
                params['last_name'] = fname
            user = User.objects.create_user(username, None, email, **params)
    return user
