import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, CharField
from django.contrib.auth.models import User
from django.forms import PasswordInput


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(ModelForm):
    password_rep = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password_rep']

    def clean(self):
        cd = self.cleaned_data
        password, password_rep = cd.get('password'), cd.get('password_rep')

        error = None
        if password != password_rep:
            error = 'Error: passwords do not match!'
        elif not bool(re.search(r'\d', password)):
            error = 'Error: password should contain at least 1 digit!'
        elif not bool(re.search(r'[A-Z]', password)):
            error = 'Error: password should contain at least 1 uppercase character!'
        elif len(password) < 8:
            error = 'Error: the length of the password should be at least 8!'

        if error:
            raise ValidationError({'password': error})

        return cd

    def save(self, commit=True):
        return super(RegisterForm, self).save(commit=commit)
