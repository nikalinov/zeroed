from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Language, Blog, Author, Comment, ContentType


def index(request):
    """View function for home page of site."""

    num_blogs = Blog.objects.count()
    num_authors = Author.objects.count()
    num_comments = Comment.objects.count()
    num_blogs_with_us_authors = Blog.objects.filter(author__country__exact='US').count()
    num_how_blogs = Blog.objects.filter(title__icontains='how').count()

    context = {
        'num_blogs': num_blogs,
        'num_authors': num_authors,
        'num_comments': num_comments,
        'num_blogs_with_us_authors': num_blogs_with_us_authors,
        'num_how_blogs' : num_how_blogs,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog
