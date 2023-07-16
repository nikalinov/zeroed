from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from .forms import ProfileEditForm, BlogForm, ContactForm
from .models import Blog
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView


def index(request):
    """View function for home page of site."""
    return render(request, 'feed/index.html')


def about(request):
    return render(request, 'feed/about.html')


class ContactFormView(LoginRequiredMixin, FormView):
    template_name = 'feed/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-success')


def contact_success(request):
    return render(request, 'feed/contact_success.html')


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

            user_profile.website = form.cleaned_data['website']
            user_profile.github = form.cleaned_data['github']
            user_profile.instagram = form.cleaned_data['instagram']
            user_profile.twitter = form.cleaned_data['twitter']
            user_profile.facebook = form.cleaned_data['facebook']

            user_profile.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('profile'))

    else:
        form = ProfileEditForm(
            initial={
                'first_name': user_profile.user.first_name,
                'last_name': user_profile.user.last_name,
                'email': user_profile.user.email,
                'website': user_profile.website,
                'github': user_profile.github,
                'instagram': user_profile.instagram,
                'twitter': user_profile.twitter,
                'facebook': user_profile.facebook,
            }
        )

    context['form'] = form
    return render(request, 'feed/profile_edit.html', context=context)


class BlogListView(ListView):
    model = Blog
    paginate_by = 5


def follow(request, pk):
    User.objects.get(pk=pk).userprofile.followers.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def unfollow(request, pk):
    User.objects.get(pk=pk).userprofile.followers.remove(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def blog_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.views += 1
    blog.save()
    context = {'blog': blog}
    return render(request, 'feed/blog.html', context=context)


def rate_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.pk)
    if user in blog.upvoters.all():
        blog.upvoters.remove(User.objects.get(pk=request.user.pk))
    else:
        blog.upvoters.add(User.objects.get(pk=request.user.pk))
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = 'feed/blog_form.html'

    def get_success_url(self):
        return reverse_lazy('blog', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']
    success_url = reverse_lazy('blog', kwargs={'pk': model.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    # TODO kwargs={pk: user.pk}
    success_url = reverse_lazy('profile')
