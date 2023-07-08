from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog


def index(request):
    """View function for home page of site."""
    return render(request, 'feed/index.html')


def about(request):
    return render(request, 'feed/about.html')


def post(request):
    return render(request, 'feed/post.html')


def contact(request):
    return render(request, 'feed/contact.html')


def profile(request, pk, sorting='title'):
    user = User.objects.get(pk=pk)
    reverse_sorting = {'rating', 'views', 'post_date'}

    if sorting in reverse_sorting:
        sorting = '-' + sorting

    blogs_sorted = user.blog_set.order_by(sorting).all()
    context = {'passed_user': user, 'blogs_sorted': blogs_sorted}
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


def follow(request, pk):
    User.objects.get(pk=pk).userprofile.followers.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def unfollow(request, pk):
    User.objects.get(pk=pk).userprofile.followers.remove(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
