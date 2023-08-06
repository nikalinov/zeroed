from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from miniblog.settings import env
from .forms import ProfileEditForm, BlogForm, ContactRequestForm
from .models import Blog, Comment, UserProfile
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
import bleach


def blogs_sorted(sorting, author=None):
    reverse_sorting = {'rating', 'views', 'post_date'}

    if sorting in reverse_sorting:
        sorting = '-' + sorting

    if sorting == '-rating':
        blogs = Blog.objects.annotate(rating=Count('upvoters')).order_by(sorting).all()
    else:
        blogs = Blog.objects.order_by(sorting).all()

    return blogs.filter(author=author) if author else blogs


class BlogListView(ListView):
    model = Blog
    paginate_by = 5
    template_name = 'feed/index.html'

    def get_queryset(self):
        # TODO fix upvotes, rating, post_date
        if 'sorting' in self.kwargs:
            return Blog.objects.order_by(self.kwargs['sorting'])
        else:
            return Blog.objects.order_by('title')


def about(request):
    return render(request, 'feed/about.html')


class ContactFormView(LoginRequiredMixin, FormView):
    template_name = 'feed/contact_form.html'
    form_class = ContactRequestForm
    success_url = reverse_lazy('contact-success')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        contact_request = form.save(commit=False)
        contact_request.sender = self.request.user
        contact_request.save()

        # TODO use SendGrid or smth for alternate from_email
        send_mail(
            subject=contact_request.subject,
            from_email=contact_request.sender.email,
            recipient_list=[env('EMAIL_HOST_USER')],
            message=contact_request.message,
        )
        return HttpResponseRedirect(self.get_success_url())


def contact_success(request):
    context = {'username': request.user.username}
    return render(request, 'feed/contact_success.html', context=context)


def profile(request, pk, sorting='title', edit=''):
    user = get_object_or_404(User, pk=pk)
    user_profile = user.userprofile

    context = {
        'passed_user': user,
        'blogs': blogs_sorted(sorting, user),
        'edit': False
    }
    if not edit:
        return render(request, 'feed/profile.html', context=context)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST)

        if form.is_valid():
            user_profile.user.first_name = form.cleaned_data['first_name']
            user_profile.user.last_name = form.cleaned_data['last_name']
            user_profile.bio = form.cleaned_data['bio']
            user_profile.user.email = form.cleaned_data['email']
            user_profile.location = form.cleaned_data['location']

            user_profile.website = form.cleaned_data['website']
            user_profile.github = form.cleaned_data['github']
            user_profile.instagram = form.cleaned_data['instagram']
            user_profile.twitter = form.cleaned_data['twitter']
            user_profile.facebook = form.cleaned_data['facebook']

            user_profile.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('profile', kwargs={'pk': pk}))

    else:
        form = ProfileEditForm(
            initial={
                'first_name': user_profile.user.first_name,
                'last_name': user_profile.user.last_name,
                'email': user_profile.user.email,
                'location': user_profile.location,
                'bio': user_profile.bio,
                'website': user_profile.website,
                'github': user_profile.github,
                'instagram': user_profile.instagram,
                'twitter': user_profile.twitter,
                'facebook': user_profile.facebook,
            }
        )

    context['form'] = form
    context['edit'] = True
    return render(request, 'feed/profile.html', context=context)


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


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    template_name = 'feed/blog.html'

    def get_success_url(self):
        return f"{reverse_lazy('blog', args=[self.kwargs['blog_pk']])}#comment-section"

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse_lazy('index'))

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post_date = datetime.now()
        comment.blog = Blog.objects.get(pk=self.kwargs['blog_pk'])
        return super().form_valid(form)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return f"{reverse_lazy('blog', args=[self.kwargs['blog_pk']])}#comment-section"