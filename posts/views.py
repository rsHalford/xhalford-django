from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from posts.models import Post, Category, Comment
from posts.forms import PostForm, CommentForm
from django.contrib.auth.decorators import permission_required
from django.utils import timezone

class PostList(ListView):
    model = Post
    template_name = "posts.html"
    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(status=1).order_by("-published_date")
        context = {
            "posts": posts
        }
        return context

def PostDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
            "post": post,
            "comments": comments,
            "form": form,
    }
    return render(request, "post.html", context)

@permission_required('auth.view_user')
def PostNew(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.save()
            return redirect("post", slug=post.slug)
    else:
        form = PostForm()
    return render(request, "postEdit.html", {"form": form})

@permission_required('auth.view_user')
def PostEdit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.save()
            return redirect("post", slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, "postEdit.html", {"form": form})

@permission_required('auth.view_user')
def DraftList(request):
    posts = Post.objects.filter(status=0).order_by("-created_date")
    return render(request, "draft-posts.html", {"posts": posts})
