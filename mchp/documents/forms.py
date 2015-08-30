from django import forms
from django.forms import ModelForm, TextInput, ChoiceField, Select, IntegerField, ClearableFileInput

from documents.models import Document


class DocumentUploadForm(ModelForm):

    PRICE_WIDGET = TextInput(attrs=dict({
        'placeholder':'type a price in points, ex: 500 would be $5.00',
        'data-toggle':'tooltip',
        'data-placement':'right',
        'data-original-title':'The average document sells for 500 points. Type a number!',
        'container_id': 'document_price',
        'class': 'form-control input-lg',
    }))

    # Price is not required in case Document is Syllabus
    # In which case automatically settings price to 0
    price = IntegerField(required=False, min_value=0, widget=PRICE_WIDGET)

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

        # Syllabus is always free
        if cleaned_data['type'] == Document.SYLLABUS:
            cleaned_data['price'] = 0
        elif 'price' not in cleaned_data:
            self.add_error('price', 'This field is required')

        return cleaned_data

    class Meta:
        model = Document
        fields = ['type', 'title', 'description', 'course', 'price', 'document']

        input_attr = {
            'class': 'form-control input-lg',
        }
        widgets = {
            # dict(x.items() | y.items()) combines the _base attrs with 
            # any class specific attrs, like the placeholder
            'title': TextInput(attrs=dict({
                'placeholder': 'ex: Exam 1 Study Guide or Syllabus',
                'data-toggle':'tooltip',
                'data-placement':'right',
                'data-original-title':'Document title only. Please don\'t include the name of the class'
            }.items() | input_attr.items())),

            'description': TextInput(attrs=dict({
                'placeholder':'a description of this document',
                'data-toggle':'tooltip',
                'data-placement':'right',
                'data-original-title':'Tell classmates what this document is'
            }.items() | input_attr.items())),

            'course': Select(attrs=dict({
                'class': 'form-control input-lg dropdown-toggle',
                'id': 'document_course',
                'data-toggle':'tooltip',
                'data-placement':'right',
                'data-original-title':'Which course does the document belong to?'
            }.items())),

            'type': Select(attrs=dict({
                'class': 'form-control input-lg dropdown-toggle',
                'id': 'document_type',
                'data-toggle':'tooltip',
                'data-placement':'right',
                'data-original-title':'Is this a Study Guide or Syllabus?'
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
