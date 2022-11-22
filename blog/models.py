from django.db import models

# Create your models here.
class Author(models.Model):
     first_name =models.CharField(max_length=40)
     last_name =models.CharField(max_length=15)
     email =models.CharField(max_length=20)

class Tag(models.Model):
     caption =models.CharField(max_length=8)

class Post(models.Model):
     
     title =models.CharField(max_length=50)
     image =models.CharField(max_length=30)
     author =models.ForeignKey(Author, on_delete=models.CASCADE)
     date = models.DateField()
     excerpt =models.CharField(max_length=100)
     content =models.CharField(max_length=2000)
     tag = models.ManyToManyField(Tag)
     slug =models.SlugField(max_length=55)
     



