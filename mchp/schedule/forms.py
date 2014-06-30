from django.forms import ModelForm,TextInput
from schedule.models import Course
import logging
logger = logging.getLogger(__name__)

class CourseCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CourseCreateForm, self).clean()
        cleaned_data['dept'] = cleaned_data['dept'].upper()
        prof =  cleaned_data['professor'].strip().lower().capitalize()
        cleaned_data['professor'] = prof
        return cleaned_data

    def as_style(self):
        return self._html_output(
            normal_row = '\
            <div class="form-group">\
            <div class="form-addon">\
            <span class="form-group-addon">%(label)s</span></div>\
            %(field)s\
            %(help_text)s</div>',
            error_row = '%s',
            row_ender = '',
            help_text_html = '%s',
            errors_on_separate_row = True)

    class Meta:
        model = Course
        fields = ['dept', 'course_number', 'professor']
        widgets = {
            'dept': TextInput(attrs={'class': 'form-control'}),
            'course_number': TextInput(attrs={'class': 'form-control'}),
            'professor': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'dept': 'Course Abbreviation',
        }
        error_messages = {
            'dept': {
                'max_length': 'Course Abbreviation is too long.',
                'required': 'Please enter a course abbreviation.',
            },
            'course_number': {
                'invalid': 'Enter only the course number.',
                'required': 'Please enter a course number.',
                'max_value': 'That course number is too large.',
                'min_value': 'That course number is too small.',
            },
            'professor': {
                'required': 'Please enter a Professor\'s name',
            },
        }
