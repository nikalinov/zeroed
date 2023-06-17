from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models
from feed.countries import COUNTRIES
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, choices=COUNTRIES, default='US')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})


class ContentType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Language(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language


class Blog(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, null=True)
    post_date = models.DateField(default=now)
    content_type = models.ManyToManyField(ContentType)
    language = models.ForeignKey(Language, on_delete=models.RESTRICT, null=True)
    content = models.TextField()

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})

    def get_content_type(self):
        return ', '.join(str(cont_type) for cont_type in self.content_type.all())


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=1000)
    post_date = models.DateField(default=now)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-post_date']
