from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog, Comment


def index(request):
    """View function for home page of site."""
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'index.html', context=context)


class AuthorListView(ListView):
    model = Blog.objects.select_related('author')


class UserDetailView(DetailView):
    model = User


class BlogListView(ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(DetailView):
    model = Blog


@login_required
# @permission_required(feed.can_write, raise_exception=True)
def write_view(request):
    pass
