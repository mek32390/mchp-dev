from django.forms import ModelForm,TextInput
from schedule.models import Course

class _BaseCourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_BaseCourseForm, self).__init__(*args, **kwargs)

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

class CourseCreateForm(_BaseCourseForm):

    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CourseCreateForm, self).clean()
        if 'dept' in cleaned_data:
            cleaned_data['dept'] = cleaned_data['dept'].upper()
        if 'professor' in cleaned_data:
            prof =  cleaned_data['professor'].strip().lower().capitalize()
            cleaned_data['professor'] = prof
        return cleaned_data

    class Meta:
        model = Course
        fields = ['dept', 'course_number', 'professor']
        widgets = {
            'dept': TextInput(attrs={'class': 'form-control input-lg'}),
            'course_number': TextInput(attrs={'class': 'form-control input-lg'}),
            'professor': TextInput(attrs={'class': 'form-control input-lg'}),
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

class CourseAddForm(_BaseCourseForm):

    def __init__(self, *args, **kwargs):
        super(CourseAddForm, self).__init__(*args, **kwargs)


