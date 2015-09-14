from django import forms
from django.forms.models import formset_factory, inlineformset_factory

from . import models


class RosterEventForm(forms.Form):
    # The placeholder magic number is a bit shitty, but see roster_upload.js and roster_submit_form.html why
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control event-title', 'placeholder': 'Exam or Assignment Title'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control event-date', 'placeholder': 'Exam or Assignment date'}))

RosterEventFormSet = formset_factory(RosterEventForm)

class RosterSubmitForm(forms.Form):
    """ Custom form for roster submission.

    Notes
    -----
    Not a model form since we process submitted data.

    """
    # [TODO] `course` should be a ChoiceField
    #        The problem with doing that is that getting a current list
    #        of courses requires putting a callable here, which in turn
    #        requires Django 1.8+.  As of time of writing (2015-07-03),
    #        MCHP is built on Django 1.7. -am
    document = forms.FileField()
    course = forms.IntegerField()
    course_name = forms.CharField()
    emails = forms.CharField(widget=forms.Textarea)
    roster_html = forms.CharField(widget=forms.Textarea)

    RosterEventFormSet = formset_factory(RosterEventForm)

    events = RosterEventFormSet()

    class Meta:
        fields = '__all__'


# class RosterReviewForm(forms.Form):
#     status = forms.ChoiceField(choices=models.Roster.STATUS_CHOICES)
#
#     class Meta:
#         fields = '__all__'
