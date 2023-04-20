from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.StartingPage.as_view(), name="starting_page"),
    path("posts", views.Posts.as_view(), name="posts"),
    path("about", views.About.as_view(), name="about"),
    path("contact", views.Contact.as_view(), name="contact"),
    path("posts/to_read", views.PostsToRead.as_view(), name="to_read"),
    path("posts/send", views.AddToRead.as_view(), name="session"), #parametr slug przekazywany do funckji
    path("posts/<slug:slug>", views.SinglePost.as_view(), name="single_post"), #parametr slug przekazywany do funckji
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
