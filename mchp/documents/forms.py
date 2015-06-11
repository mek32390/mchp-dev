from django import forms
from django.forms import ModelForm, TextInput
from django.shortcuts import get_object_or_404
from schedule.models import Course
from .models import Document, Syllabus, Roster


class DocumentUploadForm(ModelForm):

    # {{ form.as_style }} with use this in templates
    def as_style(self):
        return self._html_output(
            normal_row = '\
            <div class="form-group">\
            <div class="input-group">\
            <span class="input-group-addon">%(label)s</span>\
            %(field)s\
            %(help_text)s</div></div>',
            error_row = '%s',
            row_ender = '',
            help_text_html = '%s',
            errors_on_separate_row = True)

    def clean(self):
        cleaned_data = super(DocumentUploadForm, self).clean()
        return cleaned_data

    class Meta:
        model = Document
        fields = ['title', 'description', 'course', 'price', 'document']

        input_attr = {
            'class': 'form-control input-lg',
        }
        widgets = {
            # dict(x.items() | y.items()) combines the _base attrs with 
            # any class specific attrs, like the placeholder
            'title': TextInput(attrs=dict({
                'placeholder': 'ex: Exam 1 Study Guide',
                'data-toggle':'tooltip',
                'data-placement':'right',
                'data-original-title':'Document title only. Please don\'t include the name of the class'
            }.items() | input_attr.items())),

            'description': TextInput(attrs=dict({
                'placeholder':'Short description of this file',
                'data-toggle':'tooltip',
                'data-placement':'right',
                'data-original-title':'What you say here will help convince your classmates to buy this'
            }.items() | input_attr.items())),

            'price': TextInput(attrs=dict({
                'placeholder':'type a price in points, ex: 400 would be $4.00',
                'data-toggle':'tooltip',
                'data-placement':'right',
                'data-original-title':'The average document sells for 400 points. Type a number!'
            }.items() | input_attr.items())),
            'course': TextInput(attrs=dict({
                'placeholder':'type a course code and number: CSC 245',
                'autocomplete': 'off',
                'data-toggle': 'dropdown',
                'class': 'form-control input-lg dropdown-toggle'
            }.items())),
        }

        labels = {
            'title': 'Title',
            'description': 'Description',
            'price': 'Sell for',
            'document': 'File',
        }
        error_messages = {
            'title': {
                'max_length': 'That title is unreasonably long.',
                'required': 'That title is unreasonably short',
            },
            'price': {
                'invalid': 'That is not a price.',
            },
            'description': {
                'max_length': 'Tone it down there, Tolstoy.'
            },
            'document': {
                'required': 'Please select a file.',
            },
        }


class CourseSetUploadForm(forms.Form):
    def make_choices(self):
        """ Either an iterable (e.g., a list or tuple) of 2-tuples to use as choices for this field, or a callable that returns such an iterable. This argument accepts the same formats as the choices argument to a model field. See the model field reference documentation on choices for more details. If the argument is a callable, it is evaluated each time the field’s form is initialized."""       
        courses = Course.objects.all()
        # courses = Course.objects.filter(...)
        return [(course.name, course.pk) for course in courses]

    course = forms.ChoiceField(choices=make_choices)
    roster = forms.TextField(widget=forms.TextArea, required=False)
    syllabus = forms.FileField(required=False)

    def make_models(self):
        course = get_object_or_404(Course, pk=self.cleaned_data['course'])

        roster = self.cleaned_data.get('roster')
        syllabus = self.cleaned_data.get('syllabus')
        syllabus_name = '{} Syllabus'.format(course.name)

        if syllabus:
            Syllabus.objects.create(course=course, name=syllabus_name,
                                    document=syllabus)
        if roster:
            Roster.objects.create(course=course, html=roster)
