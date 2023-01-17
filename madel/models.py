from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
