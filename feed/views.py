from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog, Comment


def index(request):
    """View function for home page of site."""

    num_blogs = Blog.objects.count()
    num_authors = Blog.objects.select_related('author').all()
    num_comments = Comment.objects.count()
    num_blogs_with_us_authors = Blog.objects.filter(author__userprofile__location__exact='US').count()
    num_how_blogs = Blog.objects.filter(title__icontains='how').count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_blogs': num_blogs,
        'num_authors': num_authors,
        'num_comments': num_comments,
        'num_blogs_with_us_authors': num_blogs_with_us_authors,
        'num_how_blogs': num_how_blogs,
        'num_visits': num_visits,
    }
    # Render the HTML template index.html with the data in the context variable
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
