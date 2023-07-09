from random import choice
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.db import models
from feed.countries import COUNTRIES
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    reputation = models.IntegerField(default=0)
    location = models.CharField(max_length=100, choices=COUNTRIES, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    followers = models.ManyToManyField(User, related_name='followers')

    website = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})

    @property
    def blog_types(self):
        blog_types = {'ent', 'study'}
        for blog in self.user.blog_set:
            blog_types.update(blog.content_type)
        return blog_types


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class ContentType(models.Model):
    type = models.CharField(max_length=100)
    # assigning random Bulma tag color to blog type when created
    TAG_COLORS = [
        ("primary", "primary"),
        ("info", "info"),
        ("link", "link"),
        ("success", "success"),
        ("black", "black"),
        ("dark", "dark"),
        ("light", "light"),
        ("white", "white"),
        ("warning", "warning"),
        ("danger", "danger"),
    ]

    color = models.CharField(
        max_length=20, choices=TAG_COLORS, default=choice(TAG_COLORS),
    )

    def __str__(self):
        return self.type


class Language(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language


class Blog(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
    )
    post_date = models.DateField(default=now)
    content_type = models.ManyToManyField(ContentType)
    language = models.ForeignKey(Language, on_delete=models.RESTRICT, null=True)
    content = models.TextField()
    rating = models.IntegerField(editable=False, default=0)
    views = models.IntegerField(editable=False, default=0)

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
