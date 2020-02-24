from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views


urlpatterns = [
    #path('', views.home, name="blog-home"), #instead use below
    path('', PostListView.as_view(), name="blog-home"),# .as_view() convert a class to view
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),# .as_view() convert a class to view
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),#pk is primary key to select post number
    path('post/new/', PostCreateView.as_view(), name="post-create"),#we need a template for these
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name="blog-about")
]
