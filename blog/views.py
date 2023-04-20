from datetime import date
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, ListView, View
from .models import Post, Comment
from .forms import CommentForm

posts_content = Post.objects.all().order_by("date")


class StartingPage(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_posts"] = posts_content
        return context


class About(TemplateView):
    template_name = "blog/about.html"


class Contact(TemplateView):
    template_name = "blog/contact.html"


class Posts(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"]


class PostsToRead(View):
    def get(self, request):
        stored_post_id_list = request.session.get("read_later")  # read session variable from database
        if stored_post_id_list is None:
            all_posts = "empty"
        else:
            all_posts = Post.objects.filter(pk__in=stored_post_id_list)

        return render(request, "blog/to_read_list.html", {
            "all_posts": all_posts
        })


class SinglePost(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        request = self.request
        read_later_list = request.session.get("read_later")
        if read_later_list is None or post.id not in read_later_list:
            read_later = "Read later"
        else:
            read_later = "Remove from List"

        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comments": Comment.objects.filter(post=post),
            "form": CommentForm(),
            "slug": slug,
            "read_later": read_later,

        }
        return render(request, "blog/single_post.html", context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comments": Comment.objects.filter(post=post),
            "form": CommentForm(),
            "slug": slug,

        }

        if form.is_valid():  # is user empty ?, id form is valid ?,
            comment = form.save(commit=False)  # creating form object to edit
            # editing the "post" field to let database know to which post it should be saved
            comment.post = post
            comment.save()
            # if not empty than redirect to thank you url
            return render(request, "blog/single_post.html", context)

        return render(request, "blog/single_post.html", context)


class AddToRead(View):
    def post(self, request):
        stored_posts = request.session.get("read_later")  # read session variable from database
        if stored_posts is None:  # first creation of empty list if there is no variable in database
            stored_posts = []
        post_id = int(request.POST['post_id'])  # getting the post id from request
        if post_id not in stored_posts:
            stored_posts.append(post_id)  # add post id to list it it's not there yet
        else:
            stored_posts.remove(post_id)  # or remove it if it is there allready
        request.session["read_later"] = stored_posts  # save this list to session variable in database
        current_post = Post.objects.get(id=post_id)                 # getting the post of that ID to get the slug
        return HttpResponseRedirect("/posts/" + current_post.slug)
