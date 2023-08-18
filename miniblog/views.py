from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from miniblog.forms import RegisterForm
from miniblog.settings import env
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mailtrap as mt
import smtplib


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
                is_active=False,
            )

            html = render_to_string(
                'registration/register_confirm_email.html',
                context={
                    'pk': new_user.pk,
                    'username': User.objects.get(pk=new_user.pk).username,
                    'protocol': 'http',
                    'domain': request.get_host(),
                }
            )
            # text alternative for email
            text = render_to_string(
                'registration/register_confirm_email_alt.html',
                context={
                    'pk': new_user.pk,
                    'username': User.objects.get(pk=new_user.pk).username,
                    'protocol': 'http',
                    'domain': request.get_host(),
                }
            )

            send_mail(
                'Account activation',
                from_email=env('EMAIL_HOST'),
                # use Mailtrap for password reset
                recipient_list=[form.cleaned_data['email']],
                message=text,
                fail_silently=False,
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
    return render(request, 'registration/register_success.html', context=context)


def register_confirm(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = True
    user.save()
    context = {'username': user.username}
    return render(request, 'registration/register_complete.html', context=context)
