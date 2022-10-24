from django.shortcuts import render
from django.http import Http404

posts_content = {

    "post1": {
        "title": "Mountains",
        "photo": "fsdfdsa/sdafas",
        "content": "FAJNIE SIE CHODZI"

    },
    "post2": {
        "title": "shopping",
        "photo": "fsdsdsa/sdafas",
        "content": "FAJNIE SIE kupuje"

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
            "photo": posts_content[slug]["photo"],
            "content": posts_content[slug]["content"],            
        })

    except:
        raise Http404("Site does not exist")