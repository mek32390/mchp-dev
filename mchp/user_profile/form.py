from django import forms

class UserSignupForm(forms.Form):
    first_name = forms.CharField(max_length=40, label='First name (*)',\
                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'autofocus': 'autofocus'}), \
                                 required=False)
    last_name = forms.CharField(max_length=40, label='Last name (*)', \
                 widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), \
                                 required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
