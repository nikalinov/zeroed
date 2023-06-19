from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.db import models
from feed.countries import COUNTRIES
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    reputation = models.IntegerField(default=0)
    location = models.CharField(max_length=100, choices=COUNTRIES, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


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
