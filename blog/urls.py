from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.starting_page, name="starting_page"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.single_post, name="single_post") #parametr slug przekazywany do funckji
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
