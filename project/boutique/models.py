from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomeUser(AbstractUser):
    phone_number = models.CharField(blank=True, null=True)
    avatar = models.ImageField(upload_to='profile_images/' ,blank=True, null=True)
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(CustomeUser, related_name="articles", on_delete=models.CASCADE)
    price = models.IntegerField()
    QUALITY_CHOICES = [(1,"1/3"),(2,"2/3"),(3,"3/3")]
    qualite = models.IntegerField(choices=QUALITY_CHOICES)
    category = models.ManyToManyField(Category, related_name='category')

    def __str__(self):
        return self.name


class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='articles_images/')

    def __str__(self):
        return self.article.name


# Create your models here.
