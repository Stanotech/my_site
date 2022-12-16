from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField()
    excerpt = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    tag = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=55)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')     # many to one
    author = models.CharField(max_length=50)
    content = models.CharField(max_length=2000)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return f"{self.author}"