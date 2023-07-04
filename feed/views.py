from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog
from miniblog.forms import RegisterForm, LoginForm


def index(request):
    """View function for home page of site."""
    return render(request, 'feed/index.html')


def about(request):
    return render(request, 'feed/about.html')


def post(request):
    return render(request, 'feed/post.html')


def contact(request):
    return render(request, 'feed/contact.html')


def profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {'passed_user': user}
    print(user.blog_set)
    return render(request, 'feed/profile.html', context=context)


class BlogListView(ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(DetailView):
    model = Blog


@login_required
# @permission_required(feed.can_write, raise_exception=True)
def write_view(request):
    pass
