from django import forms
from django.shortcuts import get_object_or_404
from schedule.models import Course
from . import models


class CourseSetUploadForm(forms.Form):
    def make_choices(self):
        """ Either an iterable (e.g., a list or tuple) of 2-tuples to use as choices for this field, or a callable that returns such an iterable. This argument accepts the same formats as the choices argument to a model field. See the model field reference documentation on choices for more details. If the argument is a callable, it is evaluated each time the field’s form is initialized."""       
        courses = None
        courses = Course.objects.filter(...)
        return [(course.name, course.pk) for course in courses]

    course = forms.ChoiceField(choices=make_choices)
    roster = forms.TextField(widget=forms.TextArea, required=False)
    syllabus = forms.FileField(required=False)

    def make_models(self):
        course = get_object_or_404(Course, pk=self.cleaned_data['course'])

        roster = self.cleaned_data.get('roster')
        syllabus = self.cleaned_data.get('roster')

        if syllabus:
            models.Syllabus.objects.create(course=course, document=syllabus)
        if roster:
            models.Roster.objects.create(course=course, html=roster)
