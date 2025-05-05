from django import forms
from . import models

class EmailForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        obj = models.Email.objects.filter(email=email,is_active = False)
        if obj:
            raise forms.ValidationError('email is deactive pls try again later')
        return email