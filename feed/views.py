from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def index():
    pass


class AuthorListView(ListView):
    pass


class AuthorDetailView(DetailView):
    pass


class BlogListView(ListView):
    pass


class BlogDetailView(DetailView):
    pass

