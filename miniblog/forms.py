from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms import PasswordInput


class RegisterForm(ModelForm):
    password_rep = PasswordInput()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        help_texts = {'password_2': _('Repeat the password.')}

    def clean(self):
        cd = self.cleaned_data

        password_1 = cd.get('password_1')
        password_2 = cd.get('password_2')

        if password_1 != password_2:
            raise ValidationError(
                {'password_1': _('Error: passwords do not match!')}
            )

        return cd

    def save(self, commit=True):
        return super(RegisterForm, self).save(commit=commit)
