from datetime import date
from django.shortcuts import render
from django.http import Http404
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic.detail import DetailView
from django.views.generic import ListView

posts_content = Post.objects.all().order_by("date")


def starting_page(request):
    latest_posts = posts_content
    return render(request, "blog/index.html", {
        # passing all post(posts_content) variable to index.htmp
        "all_posts": latest_posts,
    })


def posts(request):
    latest_posts = posts_content
    return render(request, "blog/all_posts.html", {
        # passing all post(posts_content) variable to index.htmp
        "all_posts": latest_posts,
    })


class single_post(DetailView):
    template_name = "blog/single_post.html"
    model = Post

    def get_context_data(self, **kwargs):
        wanted_post = next(post for post in posts_content if self.kwargs["slug"]== post.slug)
        context = super().get_context_data(**kwargs)
        context["title"] = wanted_post.title
        context["image"] = wanted_post.image
        context["author"] = wanted_post.author
        context["date"] = wanted_post.date
        context["excerpt"] = wanted_post.excerpt
        context["content"] = wanted_post.content
        context["comments"] = Comment.objects.all()
        context["form"] = CommentForm()
        
        return context
