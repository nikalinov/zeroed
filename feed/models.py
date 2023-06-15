import datetime
from django.db import models
from feed.countries import COUNTRIES
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, choices=COUNTRIES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})


class ContentType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.type}'


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    post_date = models.DateField(default=datetime.date.today())
    content_type = models.ManyToManyField(ContentType)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
