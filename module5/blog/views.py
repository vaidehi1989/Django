from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from . models import Post

# Class - Based Views

# List all the Posts
class BlogListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "listblogs.html"

# View a specific post
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# Function - Based Views

# List all the Posts
def blogListView(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'listblogs.html', {'posts': posts})


# View a specific post
def blogDetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})







