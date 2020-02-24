from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #in order to create a post login is required
from .models import Post #import post class from models
from django.contrib.auth.models import User


def home(request):#insetead we can use ListView class view instead of function
    #return HttpResponse("<h1>This home Page</h1>")
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):#alternate to home function
    #setting some variables/ overwriting them in the Class
    model = Post #Post is the class in model
    template_name = 'blog/home.html'
    context_object_name = 'posts'#just like posts key in the dictionary in home function
    ordering = ['-date_posted']#this will set the order of post in home view, - means descending
    paginate_by = 5#2 posts per page


class UserPostListView(ListView):#When you click on the username above a post in the site this class will display you the posts by that user only
    #setting some variables/ overwriting them in the Class
    model = Post #Post is the class in model
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'#just like posts key in the dictionary in home function
    paginate_by = 5#2 posts per page

    def get_queryset(self):#to query all post based on author
        user = get_object_or_404(User, username=self.kwargs.get('username'))#and of the user exists then ,self.kwargs.get('username' is to get the username from the ulr in the website
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    #setting some variables/ overwriting them in the Class
    model = Post #instance is set.Post is the class in model


class PostCreateView(LoginRequiredMixin, CreateView):#LoginRequiredMixin redirects you to login page when try to create a post without logged in
    #setting some variables/ overwriting them in the Class
    model = Post #instance is set.Post is the class in model
    fields = ['title', 'content']

    def form_valid(self, form):#overwrite the function
        #form.instance.author = self.request.user #this tells that the form you are about to submit in creatpost before doing that take instance as the current logged in author/user
        form.instance.author = self.request.user
        return super().form_valid(form)#return the overwrite form


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):#LoginRequiredMixin redirects you to login page when try to create a post without logged in. UserPassesTestMixin allows only the user to update his own blog post
    #setting some variables/ overwriting them in the Class
    model = Post #instance is set.Post is the class in model
    fields = ['title', 'content']

    def form_valid(self, form):#overwrite the function
        #form.instance.author = self.request.user #this tells that the form you are about to submit in creatpost before doing that take instance as the current logged in author/user
        form.instance.author = self.request.user
        return super().form_valid(form)#return the overwrite form

    def test_func(self):
        post = self.get_object() #to get the exact post that we are updating
        if self.request.user == post.author:#if the current user is the author of the post
            return True
        return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    #setting some variables/ overwriting them in the Class
    model = Post #instance is set.Post is the class in model
    success_url = '/' #redirects to the home page after deleting a post

    def test_func(self):
        post = self.get_object() #to get the exact post that we are updating
        if self.request.user == post.author:#if the current user is the author of the post
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})