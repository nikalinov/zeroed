from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import Author, Language, Blog, Comment, ContentType
from django.db import models


admin.site.register(Comment)
admin.site.register(ContentType)
admin.site.register(Language)


class BlogInline(admin.TabularInline):
    model = Blog
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 8, 'cols': 40})},
    }


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country')
    inlines = [BlogInline]


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date', 'get_content_type')
    list_filter = ('content_type', 'author')

    fieldsets = (
        ('Section 1',
         {'fields': ('title', 'author', 'post_date')}),
        ('Section 2',
         {'fields': (('language', 'content_type'), 'content')}),
    )
    inlines = [CommentInline]



