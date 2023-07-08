from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.BlogListView.as_view(), name='all-blogs'),
    re_path(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    path('user/<int:pk>', views.profile, name='profile'),
    path('write/', views.write_view, name='write'),
    path('user/<int:pk>/sorted/<str:sorting>', views.profile, name='profile-sorted'),
    path('user/<int:pk>/add-follower/', views.follow, name='follow'),
    path('user/<int:pk>/remove-follower/', views.unfollow, name='unfollow'),
    path('user/<int:pk>/edit', views.profile_edit, name='profile-edit')
]
