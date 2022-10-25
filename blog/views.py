from datetime import date
from django.shortcuts import render
from django.http import Http404

posts_content = {

    "post1": {
        "title": "How to become a Python Web Developer",
        "image": "nerd.jpg",
        "author": "Stan",
        "date": date(2022, 10, 24),
        "excerpt": "Few secret simple tricks for becoming Web Dev in just a few clicks ! HR Department hates me! ",
        "content": "You just need a GitHub with projects like this: <ul> <li> Vending MAchine</li> <li> Online game </li>"
    },
    "post2": {
        "title": "How to become a Python Web Developer",
        "image": "nerd.jpg",
        "author": "Stan",
        "date": date(2022, 10, 27),
        "excerpt": "Few secret simple tricks for becoming Web Dev in just a few clicks ! HR Department hates me! ",
        "content": "You just need a GitHub with projects like this: <ul> <li> Vending MAchine</li> <li> Online game </li>"

    },    
    "post3": {
        "title": "How to become a Python Web Developer",
        "image": "nerd.jpg",
        "author": "Stan",
        "date": date(2022, 10, 21),
        "excerpt": "Few secret simple tricks for becoming Web Dev in just a few clicks ! HR Department hates me! ",
        "content": "You just need a GitHub with projects like this: <ul> <li> Vending MAchine</li> <li> Online game </li>"

    },   
}

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all_posts.html")

def single_post(request, slug):
    
    try:
        print("kapaciapa")
        print(posts_content[slug]["title"])
        return render(request, "blog/single_post.html", {
            "title": posts_content[slug]["title"],
            "image": posts_content[slug]["image"],
            "content": posts_content[slug]["content"],            
        })

    except:
        raise Http404("Site does not exist")