from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.starting_page.as_view(), name="starting_page"),
    path("posts", views.posts.as_view(), name="posts"),
    path("about", views.about.as_view(), name="about"),
    path("contact", views.contact.as_view(), name="contact"),
    path("posts/to_read", views.posts_to_read.as_view(), name="to_read"),
    path("posts/send", views.AddToRead.as_view(), name="session"), #parametr slug przekazywany do funckji
    path("posts/<slug:slug>", views.single_post.as_view(), name="single_post"), #parametr slug przekazywany do funckji
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
