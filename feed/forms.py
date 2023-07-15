from django import forms
from django.core.exceptions import ValidationError

from feed.models import Blog


class ProfileEditForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    # bio = forms.CharField(max_length=500, widget=forms.Textarea)
    email = forms.EmailField(max_length=100)
    # location = forms.CharField(max_length=100)

    website = forms.CharField(max_length=100, required=False)
    github = forms.CharField(max_length=100, required=False)
    twitter = forms.CharField(max_length=100, required=False)
    instagram = forms.CharField(max_length=100, required=False)
    facebook = forms.CharField(max_length=100, required=False)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'content_type', 'language']

    # TODO
    """
    def clean_content(self):
        content = self.cleaned_data['content']
        content_len = 100
        print(content, type(content))
        if len(content.getLength()) < content_len:
            raise ValidationError(f'There should be at least {content_len} characters in the blog!')
        return content
    """
