from django.test import TestCase
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.db.transaction import atomic
from django.conf import settings

from documents.models import Document, Upload
from documents.s3utils import S3Auth
from schedule.models import School, Course
from user_profile.models import Student

# import mock

class DocumentUtilsTest(TestCase):

    def s3_url(self):
        s = S3Auth(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        url = s.get_v2(settings.AWS_STORAGE_BUCKET_NAME, '/media/documents/1880s_uncle_grandpa.gif')
        print(url)

class DocumentModelTest(TestCase):
    def setUp(self):
        test_uni = {
            'domain': "www.test.edu", 
            'name': "Test University", 
            'phone_number':"(520) 555-5555",
            'address': "413 n What st.", 
            'city':"Test city",
            'state': 'AZ',
            'country': 'USA',
        }
        self.school = School(**test_uni)
        self.school.save()
        test_course = {
            'domain': self.school,
            'dept': 'CSC',
            'course_number': '245',
            'professor': 'test',
        }
        self.course = Course(**test_course)
        self.course.save()

        # make a document
        content = ContentFile("Test file")
        doc_data = {
            'title': 'test_doc',
            'description': 'This is a test document',
            'course': self.course,
        }
        doc = Document(**doc_data)
        doc.document.save('test.txt', content)
        doc.save()
        self.document = doc
        self.assertNotEqual(doc.document.size, 0)

    def testOnDelete(self):
        doc = self.document
        c_pk = self.course.pk
        with atomic():
            self.assertRaises(Course.DoesNotExist, Course.objects.get, dept='del')
        self.course.delete()
        with atomic():
            self.assertRaises(Course.DoesNotExist, Course.objects.get, pk=c_pk)

        c = Course.objects.get(dept='del')
        # have to retrieve the object from the db again to see its been updated
        doc = Document.objects.get(pk=doc.pk)
        self.assertEqual(doc.course, c)
        self.assertEqual(doc.course.dept, 'del')

    def testUpload(self):
        student_data = {
            'user': User.objects.create_user('test_dude'),
            'school': self.school,
        }
        student = Student(**student_data)
        student.save()
        upload = Upload(document=self.document, owner=student)
        upload.save()


class CreateUserTestCase(TestCase):
    """ Test creation of users.

    """
    # def testUserCreation(self):
    #     from utils import ensure_user_exists
    #
    #     email = 'test@example.com'
    #     user = ensure_user_exists(email)
    #     self.assertNotNull(user)
    #
    #     # e-mail address required for this method, even though not for users
    #     self.assertRaises(ValueError, ensure_user_exists, 'test')

    def testSuffix(self):
        from .utils import suffix

        name = 'john.q.public'

        self.assertEqual(suffix(name, '', 2), 'jo')
        self.assertEqual(suffix(name, 'jr', 2), 'jr')
        self.assertEqual(suffix(name, '', 8), 'john.q.p')
        self.assertEqual(suffix(name, 'jr', 8), 'john.qjr')
        self.assertEqual(suffix(name, '', 16), 'john.q.public')
        self.assertEqual(suffix(name, 'jr', 16), 'john.q.publicjr')
        with self.assertRaises(ValueError):
            suffix(name, 'jr', 1)  # suffix length cannot exceed max length

    def testIncrementalSuffixes(self):
        from .utils import incremental_suffixes

        name = 'john.q.public'
        suffixes = incremental_suffixes(name, 8)
        self.assertEqual(next(suffixes), 'john.q.p')  # no suffix here
        self.assertEqual(next(suffixes), 'john.q.2')  # one digit now
        self.assertEqual(next(suffixes), 'john.q.3')  # "
        self.assertEqual(next(suffixes), 'john.q.4')  # "
        self.assertEqual(next(suffixes), 'john.q.5')  # "
        self.assertEqual(next(suffixes), 'john.q.6')  # "
        self.assertEqual(next(suffixes), 'john.q.7')  # "
        self.assertEqual(next(suffixes), 'john.q.8')  # "
        self.assertEqual(next(suffixes), 'john.q.9')  # "
        self.assertEqual(next(suffixes), 'john.q10')  # two digits now

        suffixes = incremental_suffixes(name, 16)
        self.assertEqual(next(suffixes), 'john.q.public')   # no suffix here
        self.assertEqual(next(suffixes), 'john.q.public2')  # one digit now
        self.assertEqual(next(suffixes), 'john.q.public3')  # "
        self.assertEqual(next(suffixes), 'john.q.public4')  # "
        self.assertEqual(next(suffixes), 'john.q.public5')  # "
        self.assertEqual(next(suffixes), 'john.q.public6')  # "
        self.assertEqual(next(suffixes), 'john.q.public7')  # "
        self.assertEqual(next(suffixes), 'john.q.public8')  # "
        self.assertEqual(next(suffixes), 'john.q.public9')  # "
        self.assertEqual(next(suffixes), 'john.q.public10')  # two digits now

        suffixes = incremental_suffixes(name, 1)
        self.assertEqual(next(suffixes), 'j')  # no suffix at first
        self.assertEqual(next(suffixes), '2')  # one digit now
        self.assertEqual(next(suffixes), '3')  # "
        self.assertEqual(next(suffixes), '4')  # "
        self.assertEqual(next(suffixes), '5')  # "
        self.assertEqual(next(suffixes), '6')  # "
        self.assertEqual(next(suffixes), '7')  # "
        self.assertEqual(next(suffixes), '8')  # "
        self.assertEqual(next(suffixes), '9')  # "
        with self.assertRaises(ValueError):
            next(suffixes)                     # can't do two digits
