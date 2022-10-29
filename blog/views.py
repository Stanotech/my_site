from datetime import date
from django.shortcuts import render
from django.http import Http404

posts_content = [
    {
        "slug": "post1",
        "title": "How to become a Python Web Developer",
        "image": "nerd.jpg",
        "author": "Stan",
        "date": date(2022, 10, 24),
        "excerpt": "Few secret simple tricks for becoming Web Dev in just a few clicks ! HR Department hates me! ",
        "content": "You just need a GitHub repository with projects like this: <ul> <li> Vending MAchine</li> <li> Online pong game </li> <li> Blog site made with Django framework </li> <li> G-code generator for smoothing artefacts in your prints </li></ul>"
    },
    {
        "slug": "post2",
        "title": "Think before you do something",
        "image": "passion.jpg",
        "author": "Stan",
        "date": date(2022, 10, 27),
        "excerpt": "Some people say that our brains is for thinking, but American scientist say- Netflix is better",
        "content": "Your passion is right in front of your face. If you have to look for it, then youre probably not passionate about it at all. So screw finding your passion."

    },    
    {
        "slug": "post3",
        "title": "Should we use violence in raising parents ?",
        "image": "post-slide-4.jpg",
        "author": "Bobo",
        "date": date(2022, 10, 21),
        "excerpt": "New research shows that violence is a good way to convince parents to whatever you want",
        "content": "Just a few ideas for all kids: Brazen bull, Breaking wheel, Breast ripper, Batog, Birch rod, Catapelta[citation needed], Choke, pear, Cattle, prod, Electroshock, weapon, Gag, Garrote, Graduated, Electronic, Decelerator, Head, crusher, Instep, borer, Iron, chair, Iron, Maiden, (use, is, debated), Jiagun, /, Zanzhi, Judas, cradle, Knee, splitter, Led, sprinkler, Mancuerda, Parrilla, Pau, de, Arara, Pendulum[2], (of, disputed, historicity), Picana, Pillory, Rack, Rope, Scavenger's, daughter, Scold's, bridle, Spanish, boot, Strappado, Stocks, Tablilla, Thumbscrew, Tongue, tearer, Tramp, chair, Tucker, telephone, Whip Wooden horse"
    },   
    {
        "slug": "post4",
        "title": "How we eat is very important",
        "image": "monkey.jpg",
        "author": "Stan",
        "date": date(2022, 10, 20),
        "excerpt": "You are what you eat",
        "content": "If you eat a coconut, you will become a coconut. That's it."
    },   
]

def get_date(post):
    return post['date']

def starting_page(request):
    posts_content.sort(key=get_date)
    latest_posts = posts_content[-4:]
    return render(request, "blog/index.html", {
            "all_posts": latest_posts,             #passing all post(posts_content) variable to index.htmp
        })           

def posts(request):
    return render(request, "blog/all_posts.html")

def single_post(request, slug):
    wanted_post = next(post for post in posts_content if slug == post["slug"])  #if requested slug is equal to slug of post from dictionary than assaign this post to
    
    try:
        print("gowno")
        print(wanted_post)
        return render(request, "blog/single_post.html", {
            "title": wanted_post["title"],
            "image": wanted_post["image"],
            "author": wanted_post["author"],
            "date": wanted_post["date"],
            "excerpt": wanted_post["excerpt"],
            "content": wanted_post["content"],            
        })

    except:
        raise Http404("Site does not exist")