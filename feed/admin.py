from django.contrib import admin
from .models import Author, Language, Blog, Comment, ContentType


admin.site.register(Comment)
admin.site.register(ContentType)
admin.site.register(Language)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country')


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



