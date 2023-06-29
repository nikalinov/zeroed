from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from miniblog.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
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
