from django import forms


class RosterSubmitForm(forms.Form):
    course = forms.IntegerField()
    emails = forms.Textarea()
    roster_html = forms.TextArea()

    class Meta:
        fields = ['course', 'roster_html', 'emails']
