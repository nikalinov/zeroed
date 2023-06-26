from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog
from miniblog.forms import RegisterForm


def index(request):
    """View function for home page of site."""
    return render(request, 'feed/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            print(form.fields)
            new_user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                is_active=False
            )
            return HttpResponseRedirect(
                reverse('register-success', kwargs={'pk': new_user.pk})
            )
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context=context)


def register_success(request, pk):
    context = {'username': User.objects.get(pk=pk).username}
    return render(request, 'registration/register-success.html', context)

def about(request):
    return render(request, 'feed/about.html')


def post(request):
    return render(request, 'feed/post.html')


def contact(request):
    return render(request, 'feed/contact.html')


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
