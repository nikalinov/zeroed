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
            types[content_type.type] += 1
    return list(types.items())


@register.filter
def get_color(blog_name: str) -> str:
    tag_colors = [
        "primary", "is-info", "link", "success", "black",
        "dark", "light", "white", "warning", "danger"
    ]
    types_colors = {obj.type: choice(tag_colors) for obj in ContentType.objects.all()}
    return types_colors[blog_name]

