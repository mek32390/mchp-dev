from django.forms import ModelForm,TextInput

from documents.models import Document

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
                'placeholder': 'Document Title'
            }.items() | input_attr.items())),

            'description': TextInput(attrs=dict({
                'placeholder':'Short description of file'
            }.items() | input_attr.items())),

            'price': TextInput(attrs=dict({
                'placeholder':'ex: 500'
            }.items() | input_attr.items())),
            'course': TextInput(attrs=dict({
                'placeholder':'ex: csc 245',
                'autocomplete': 'off',
            }.items() | input_attr.items())),
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
