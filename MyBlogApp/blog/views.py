from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .models import Post
from .forms import PostForm, CommentForm


# List all the Posts
class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "listposts.html"

# List all the Posts
def postListView(request):
    posts = Post.objects.all()
    return render(request, 'listposts.html', {'posts': posts})


# View a specific post
class PostDetailView(DetailView, CreateView):
    model = Post
    template_name = 'detailview.html'
    form_class = CommentForm

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id = self.kwargs['pk'])
        return super().form_valid(form)



# View a specific post
def postDetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detailview.html', {'post': post})


# Form to add new object
@method_decorator(login_required, name='dispatch')
class PostAddView(CreateView):
    model = Post
    template_name = 'formview.html'
    form_class = PostForm
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(PostAddView, self).get_context_data(**kwargs)
        context['heading'] = "Add Post"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Form to add new object
@login_required
def postAddView(request):
    if request.user.is_authenticated:
        heading = 'Add Post'
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save()
                post.author = request.user
                post.save()
                return redirect('detailview', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'formview.html', {'form': form, 'heading': heading})
    else:
        return redirect('login')


# Form to update object
@method_decorator(login_required, name='dispatch')
class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'formview.html'
    login_url = 'login'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostEditView, self).get_context_data(**kwargs)
        context['heading'] = "Edit Post"
        return context


# Form to update object
def postEditView(request, pk):
    if request.user.is_authenticated:
        heading = 'Edit Post'
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('detailview', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'formview.html', {'form': form, 'heading': heading})
    else:
        return redirect('login')


# Delete a Post(always works with post method)
@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = None
    success_url = reverse_lazy('listposts')
    login_url = 'login'


# Delete a post
def postDeleteView(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('listposts')
    else:
        return redirect('login')
