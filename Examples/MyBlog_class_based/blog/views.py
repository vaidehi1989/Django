from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Post, Comment
from .forms import PostForm, CommentForm


# List all the Posts
class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "listposts.html"


# View a specific post
class PostDetailView(DetailView, CreateView):
    model = Post
    template_name = 'detailview.html'
    form_class = CommentForm

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id = self.kwargs['pk'])
        return super().form_valid(form)

# Form to add new object
@method_decorator(login_required, name='dispatch')
class PostAddView(CreateView):
    model = Post
    template_name = 'formview.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super(PostAddView, self).get_context_data(**kwargs)
        context['heading'] = "Add Post"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Form to update object
@method_decorator(login_required, name='dispatch')
class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'formview.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostEditView, self).get_context_data(**kwargs)
        context['heading'] = "Edit Post"
        return context


# Delete a Post(always works with post method)
@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = None
    success_url = reverse_lazy('listposts')
