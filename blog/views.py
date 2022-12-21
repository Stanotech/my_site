from datetime import date
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

from django.views.generic import CreateView, TemplateView, ListView
from django.views import View

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


class single_post(View):


  

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "title": post.title,
            "image": post.image,
            "author": post.author,
            "date": post.date,
            "excerpt": post.excerpt,
            "content": post.content,
            "comments": Comment.objects.filter(post = post),
            "form": CommentForm(),
            "post": post,
            "post_tags": post.tag.all(),
            "slug": slug,
        }
        return render(request, "blog/single_post.html", context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        context = {
            "form": form,
            "title": post.title,
            "image": post.image,
            "author": post.author,
            "date": post.date,
            "excerpt": post.excerpt,
            "content": post.content,
            "comments": Comment.objects.filter(post = post),
            "form": CommentForm(),
            "post": post,
            "post_tags": post.tag.all(),
            "slug": slug,
         }

        if form.is_valid():  # is user empty ?, id form is valid ?,
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # if not empty than redirect to thank you url
            return render(request, "blog/single_post.html", context)

        return render(request, "blog/single_post.html", context)