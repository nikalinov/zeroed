from django.conf.urls.static import static
from django.urls import path
from miniblog import settings
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='index'),
    path('sorted/<str:sorting>', views.BlogListView.as_view(), name='index-sorted'),
    path('about/', views.about, name='about'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('contact/success', views.contact_success, name='contact-success'),
    path('blogs/', views.BlogListView.as_view(), name='all-blogs'),
    path('blog/<int:pk>', views.blog_view, name='blog'),
    path('user/<int:pk>/', views.profile, name='profile'),
    path('user/<int:pk>/sorted/<str:sorting>', views.profile, name='profile-sorted'),
    path('user/<int:pk>/add-follower/', views.follow, name='follow'),
    path('user/<int:pk>/remove-follower/', views.unfollow, name='unfollow'),
    path('user/<int:pk>/<str:edit>', views.profile, name='profile-edit'),
    path('blog/<int:pk>/rate', views.rate_view, name='rate'),
    path('blog/create', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog-delete'),
    path('blog/<int:blog_pk>/add-comment', views.CommentCreateView.as_view(), name='comment-add'),
    path('blog/<int:blog_pk>/delete-comment/<int:pk>', views.CommentDeleteView.as_view(), name='comment-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
