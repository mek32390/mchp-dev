from django.db import models, connection

import schedule.models

class CourseManager(models.Manager):
    '''
    List of courses for a student
    '''
    def get_classes_for(self, student):
        courses = schedule.models.Course.objects.filter(
            enrollment__student=student,
        ).order_by('dept', 'course_number', 'professor')
        return courses

    def get_classes_in_common(self, student1, student2):
        cursor = connection.cursor()
        # simple self join 
        cursor.execute(
            "select distinct e1.course_id \
            from schedule_enrollment e1, schedule_enrollment e2 \
            where e1.course_id = e2.course_id \
            and e1.student_id <> e2.student_id \
            and e1.student_id = %s \
            and e2.student_id = %s", 
            [student1.pk, student2.pk],
        )
        courses = cursor.fetchall()
        # [(pk,), (pk,), ...] -> [pk, pk, ...]
        course_list = [pk for row in courses for pk in row]

        # fetch all courses as actual model objects
        courses = schedule.models.Course.objects.filter(
            pk__in=course_list
        )
        return courses

    '''
    Classmate list for a student, for either one course or all the courses the student is in
    '''
    def get_classmates_for(self, student, course=None):
        # student is not enrolled in the class, return None
        if not schedule.models.Enrollment.objects.filter(
            student=student,
        ).exists():
            return None
        # list for a single course
        courses = []
        if course:
            courses = [course]
        else:
            # list for all courses student is in
            courses = student.courses
        classmates = []
        for course in courses:
            classmates += self.get_classlist_for(course, exclude_student=student)
        return classmates

    '''
    List of students in a class
    '''
    def get_classlist_for(self, course, exclude_student=None):
        enrolls = schedule.models.Enrollment.objects.filter(
            course=course
        ).exclude(
            student=exclude_student
        )
        return [enroll.student for enroll in enrolls]
