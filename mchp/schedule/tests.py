from django.test import TestCase
from django.db.utils import IntegrityError
from django.db.transaction import atomic
from schedule.models import School, Course
from schedule.forms import CourseCreateForm

class ScheduleModelFormTests(TestCase):
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

    def testCourseCreate(self):
        form_data = {
            'dept': 'csc',
            'course_number': '245',
            'professor': 'mccann',
        }

        form = CourseCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.instance.dept, 'CSC')

        course = form.save(commit=False)
        course.domain = self.school
        course.save()

        self.assertEqual(
            Course.objects.get(id=form.instance.id).dept,
            'CSC'
        )

class DatabaseTestCase(TestCase):

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


    def testCourseMinMax(self):
        data = {
            'domain': self.school,
            'dept': 'CSC',
            'course_number': '78',
            'professor': 'mccann',
        }
        c = Course(**data)
        c.save()
        other = Course(**data)
        with atomic():
            self.assertRaises(IntegrityError, other.save)
        data['course_number'] = '100000'
        c = Course(**data)
        c.save()
        other = Course(**data)
        with atomic():
            self.assertRaises(IntegrityError, other.save)


    def testCourseUnique(self):
        data = {
            'domain': self.school,
            'dept': 'CSC',
            'course_number': '245',
            'professor': 'mccann',
        }
        c = Course(**data)
        c.save()
        other = Course(**data)
        with atomic():
            self.assertRaises(IntegrityError, other.save)

    def testEDUValidation(self):
        from django.forms import ModelForm

        class TestForm(ModelForm):
            class Meta:
                model = School
                fields = '__all__'

        post = { 
            'domain': "www.google.com", 
            'name': "Test University", 
            'phone_number':"(520) 555-5555",
            'address': "413 n What st.", 
            'city':"Test city"
        }
        test_school = School()
        test_school_form = TestForm(instance=test_school)
        self.assertEqual(test_school_form.is_valid(), False)
        test_school_form = TestForm(post, instance=test_school)
        self.assertEqual(test_school_form.is_valid(), False)

        post['domain'] = 'www.test.edu'
        test_school = School()
        test_school_form = TestForm(post, instance=test_school)
        self.assertEqual(test_school_form.is_valid(), True)
