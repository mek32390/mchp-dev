from django.forms import ModelForm,TextInput
from schedule.models import Course

class CourseCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields['dept'].label = "Course Abbreviation"
        self.fields['dept'].widget=TextInput(attrs={'class': 'form-control'})
        self.fields['course_number'].widget=TextInput(attrs={'class': 'form-control'})
        self.fields['professor'].widget=TextInput(attrs={'class': 'form-control'})

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
            help_text_html = ' %s',
            errors_on_separate_row = False)

    class Meta:
        model = Course
        fields = ['dept', 'course_number', 'professor']
