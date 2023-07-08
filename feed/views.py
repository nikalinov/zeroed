from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ProfileEditForm
from .models import Blog, UserProfile


def index(request):
    """View function for home page of site."""
    return render(request, 'feed/index.html')


def about(request):
    return render(request, 'feed/about.html')


def post(request):
    return render(request, 'feed/post.html')


def contact(request):
    return render(request, 'feed/contact.html')


def profile(request, pk, sorting='title', edit=''):
    user = get_object_or_404(User, pk=pk)
    user_profile = user.userprofile
    reverse_sorting = {'rating', 'views', 'post_date'}

    if sorting in reverse_sorting:
        sorting = '-' + sorting

    blogs_sorted = user.blog_set.order_by(sorting).all()
    context = {'passed_user': user, 'blogs_sorted': blogs_sorted}
    if not edit:
        return render(request, 'feed/profile.html', context=context)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST)

        if form.is_valid():
            user_profile.user.first_name = form.cleaned_data['first_name']
            user_profile.user.last_name = form.cleaned_data['last_name']
            user_profile.bio = form.cleaned_data['bio']
            user_profile.user.email = form.cleaned_data['email']

            for resource, user_contact in form.cleaned_data['contacts'].items():
                user_profile.contacts[resource] = user_contact

            user_profile.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('profile'))

    else:
        form = ProfileEditForm(
            initial={
                'first_name': user_profile.user.first_name,
                'last_name': user_profile.user.last_name,
                'bio': user_profile.bio,
                'email': user_profile.user.email,
                'contacts': dict(**user_profile.contacts)
            }
        )

    context['form'] = form
    return render(request, 'feed/profile_edit.html', context=context)


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
