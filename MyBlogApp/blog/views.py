from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Post
from .forms import PostEditForm, PostForm


# class based
class ListPosts(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'listposts.html'


# Function based
def listPosts(request):
    posts = Post.objects.all()
    return render(request, 'listposts.html', {'posts': posts})


# ----------------------------------------------------------------

def detailPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detailview.html', {'post': post})


class DetailPost(DetailView):
    model = Post
    template_name = 'detailview.html'


# ----------------------------------------------------------------

class DeletePost(DeleteView):
    model = Post
    template_name = None
    success_url = reverse_lazy('listposts')


def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('listposts')


# ----------------------------------------------------------------

def postAddView(request):
    # heading = 'Add Post'
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('detailview', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'CreateForm.html', {'form': form})










# Form to add new object
class PostAddView(CreateView):
    model = Post
    template_name = 'CreateForm.html'
    form_class = PostForm

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(PostAddView, self).get_context_data(**kwargs)
    #     context['heading'] = "Add Post"
    #     return context


# ----------------------------------------------------------------
# Form to update object
def postEditView(request, pk):
    # heading = 'Edit Post'
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('detailview', pk=post.pk)
    else:
        form = PostEditForm(instance=post)
    return render(request, 'EditForm.html', {'form': form})


# Form to update object
class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'EditForm.html'

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(PostEditView, self).get_context_data(**kwargs)
    #     context['heading'] = "Edit Post"
    #     return context