from datetime import date
from django.shortcuts import render
from django.http import Http404
from .models import Post, Comment
from .forms import CommentForm

from django.views.generic import CreateView, TemplateView, ListView

posts_content = Post.objects.all().order_by("date")


class starting_page(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_posts"] = posts_content
        return context


class posts(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"]


class single_post(CreateView):
    template_name = "blog/single_post.html"
    model = Post
    form_class = CommentForm
    succes_url = "blog/single_post.html"

    # by default view don’t know what to do with data.
    def form_valid(self, form):
        form.save()				# so please save data to database
        return super().form_valid(form)  # and return it

    def get_context_data(self, **kwargs):
        wanted_post = next(
            post for post in posts_content if self.kwargs["slug"] == post.slug)
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
