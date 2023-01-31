from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=50)


class Product(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length = 50)
    extra_inf = models.TextField()
    price = models.IntegerField()
    rate = models.FloatField(default=5)
    post_date = models.DateTimeField(auto_now_add =True)


class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_date = models.DateField(auto_now_add =True)
    post = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='Comments')

