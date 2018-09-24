from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# List all the Posts
def postListView(request):
    posts = Post.objects.all()
    return render(request, 'listposts.html', {'posts': posts})


# View a specific post
def postDetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
        return redirect('detailview', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'detailview.html', {'post': post, 'form': form})



# Delete a post
def postDeleteView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated and request.user == post.author:
        post.delete()
        return redirect('listposts')
    else:
        return redirect('/accounts/login?next='+request.path)


# Form to add new object
@login_required
def postAddView(request):
    heading = 'Add Post'
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detailview', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'formview.html', {'form': form, 'heading': heading})

# Form to update object
@login_required
def postEditView(request, pk):
    heading = 'Edit Post'
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
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
        return redirect('/accounts/login?next='+request.path)
