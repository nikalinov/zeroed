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

        if password != str(password_rep):
            raise ValidationError(
                {'password': _('Error: passwords do not match!')}
            )

        return cd

    def save(self, commit=True):
        return super(RegisterForm, self).save(commit=commit)
