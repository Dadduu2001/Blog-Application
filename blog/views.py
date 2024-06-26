from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post

# Create your views here. Static data
# posts = [
#     {
#         'author':'Sourabh Potfode',
#         'title':'Blog Post 1',
#         'content':'It is all about first Blog post',
#         'date_posted':'October 1, 2023'
#     },
#     {
#         'author':'Rishabh Khandagre',
#         'title':'Blog Post 2',
#         'content':'It is all about second Blog post',
#         'date_posted':'October 2, 2023'
#     }
# ]
def home(request):
    data_send ={
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', data_send)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted'] this has been overriden by queryset
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image_f', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','image_f', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
