from django.urls import path, include
from . import views

print("zduoy")

urlpatterns = [
    path("", views.starting_page, name="starting_page"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.single_post, name="single_post") #parametr slug przekazywany do funckji
]
