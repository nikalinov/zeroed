from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='all-blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('authors/', views.AuthorListView.as_view(), name='all-authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
