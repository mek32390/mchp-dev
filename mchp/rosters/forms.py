from django import forms
from . import models


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
    emails = forms.CharField(widget=forms.Textarea)
    roster_html = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = '__all__'


# class RosterReviewForm(forms.Form):
#     status = forms.ChoiceField(choices=models.Roster.STATUS_CHOICES)
#
#     class Meta:
#         fields = '__all__'
