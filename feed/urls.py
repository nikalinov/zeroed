from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.BlogListView.as_view(), name='all-blogs'),
    re_path(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    re_path(r'^user/(?P<pk>\d+)$', views.UserDetailView.as_view(), name='user-detail'),
    path('write/', views.write_view, name='write'),
]
