from datetime import date
from django.shortcuts import render
from django.http import Http404
from .models import Author, Post, Tag

posts_content = Post.objects.all().order_by("date")


def starting_page(request):
    latest_posts = posts_content
    return render(request, "blog/index.html", {
            "all_posts": latest_posts,             #passing all post(posts_content) variable to index.htmp
        })           

def posts(request):
    latest_posts = posts_content
    return render(request, "blog/all_posts.html", {
            "all_posts": latest_posts,             #passing all post(posts_content) variable to index.htmp
        })       
        
def single_post(request, slug):
    print(slug)
    wanted_post = next(post for post in posts_content if slug == post.slug)  #if requested slug is equal to slug of post from dictionary than assaign this post. Next convert last list object to just object outside list.
    print(wanted_post)
    try:
        return render(request, "blog/single_post.html", {
            "title": wanted_post.title,
            "image": wanted_post.image,
            "author": wanted_post.author,
            "date": wanted_post.date,
            "excerpt": wanted_post.excerpt,
            "content": wanted_post.content,            
        })

    except:
        raise Http404("Site does not exist")