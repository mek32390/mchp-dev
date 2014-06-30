from django.forms import ModelForm,TextInput
from schedule.models import Course
from user_profile.models import Student

class _BaseCourseForm(ModelForm):

    input_attr = {
        'class': 'form-control input-lg',
    }

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
            # dict(x.items() | y.items()) combines the _base attrs with 
            # any class specific attrs, like the placeholder
            'dept': TextInput(attrs=dict({
                'placeholder': 'ex: PSY'
            }.items() | _BaseCourseForm.input_attr.items())),

            'course_number': TextInput(attrs=dict({
                'placeholder':'ex: 200'
            }.items() | _BaseCourseForm.input_attr.items())),

            'professor': TextInput(attrs=dict({
                'placeholder':'ex: Doolittle'
            }.items() | _BaseCourseForm.input_attr.items())),
        }

        labels = {
            'dept': 'Course Code',
            'course_number': 'Course #',
            'professor': 'Prof Last Name',
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

    class Meta:
        model = Student 
        fields = ['courses']
