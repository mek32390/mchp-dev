from django.db import models

import schedule.models

class CourseManager(models.Manager):
    def get_classes_for(self, student):
        courses = schedule.models.Course.objects.filter(
            enrollment__student=student,
        ).order_by('dept', 'course_number', 'professor')
        return courses

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

    def get_classlist_for(self, course, exclude_student=None):
        enrolls = schedule.models.Enrollment.objects.filter(
            course=course
        ).exclude(
            student=exclude_student
        )
        return [enroll.student for enroll in enrolls]
