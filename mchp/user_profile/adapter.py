from allauth.account.adapter import DefaultAccountAdapter
from django import forms
import re

class AccountAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        p = re.compile('.*(\.edu)$', re.IGNORECASE)
        if p.match(email):
            return email
        raise forms.ValidationError("You can only sign up with a .edu address")
