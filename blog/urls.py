from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name='posts'),
    path("posts/<slug:slug>", views.single_post, name='single_post')

]
