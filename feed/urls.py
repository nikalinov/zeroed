from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.BlogListView.as_view(), name='all-blogs'),
    path('blog/<int:pk>', views.blog_view, name='blog'),
    path('user/<int:pk>', views.profile, name='profile'),
    path('write/', views.write_view, name='write'),
    path('user/<int:pk>/sorted/<str:sorting>', views.profile, name='profile-sorted'),
    path('user/<int:pk>/add-follower/', views.follow, name='follow'),
    path('user/<int:pk>/remove-follower/', views.unfollow, name='unfollow'),
    path('user/<int:pk>/<str:edit>', views.profile, name='profile-edit'),
    path('blog/<int:pk>/rate', views.rate_view, name='rate'),
    path('blog/create', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog-delete'),
]
