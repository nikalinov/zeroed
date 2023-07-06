from collections import defaultdict
from random import choice

from django import template
from django.contrib.auth.models import User
from feed.models import ContentType

register = template.Library()


@register.filter
def get_blog_types(user: User) -> list[tuple]:
    types = defaultdict(int)
    for blog in user.blog_set.all():
        for content_type in blog.content_type.all():
            types[content_type] += 1
    return list(types.items())


def sorted(blogs, key):
    return sorted(blogs, key=key)
