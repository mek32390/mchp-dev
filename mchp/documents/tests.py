from django.test import TestCase
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.db.transaction import atomic

from documents.models import Document, Upload
from schedule.models import School, Course
from user_profile.models import Student

# import mock

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
