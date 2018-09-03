from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm
#-----------------------------------------------------------------------------
# Class - Based Views
#-----------------------------------------------------------------------------
# Form to add new object
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.publish()
        return super().form_valid(form)

# Form to update object
class BlogUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'

# Delete a Post(always works with post method)
class BlogDeleteView(DeleteView):
    model = Post
    template_name = None
    success_url = reverse_lazy('viewblogs')


# List all the Posts
class BlogListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "listblogs.html"


# View a specific post
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

#-----------------------------------------------------------------------------
# Function - Based Views
#-----------------------------------------------------------------------------
# Form to add new object
def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.publish()
            post.save()
            # /blog/post/<pk>
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

# Form to update object
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_delete(request, pk):
    post= get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('viewblogs')

# List all the Posts
def blogListView(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'listblogs.html', {'posts': posts})


# View a specific post
def blogDetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
