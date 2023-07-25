from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import Textarea
from .models import Language, Blog, Comment, ContentType, UserProfile
from django.db import models


admin.site.register(Comment)
admin.site.register(ContentType)
admin.site.register(Language)


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class BlogInline(admin.TabularInline):
    model = Blog
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 8, 'cols': 40})},
    }


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, BlogInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


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



