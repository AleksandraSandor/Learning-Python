from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField()
    available = models.BooleanField(default=True)
    available_from = models.DateField(null=True)

class Opinion(models.Model):
    description = models.TextField()
    product = models.ForeignKey(Product)

class Category(models.Model):
    name = models.CharField(max_length=64) #c,null=True)
    description = models.TextField(null = True),

LIGHTSABERS = (
    (1, "w trakcie pisania"),
    (2, "czeka na akceptację redaktora"),
    (3, "opublikowany"),
)

class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=LIGHTSABERS)
    date_start = models.DateField(null = True)
    date_end = models.DateField(null=True)

scores = (
    (1, "*"),
    (2, "**"),
    (3, "***"),
    (4, "****"),
    (5, "*****"),
)


class Album(models.Model):
    title = models.CharField(max_length=128)
    date_pub = models.DateField()
    score = models.IntegerField(choices=scores)

class Discount(models.Model):
    value_in_percent=models.FloatField()
    product=models.OneToOneField(Product, on_delete=models.CASCADE,	primary_key=True)

    #relacja wiele do wielu
class OrderData(models.Model):
    description = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)

