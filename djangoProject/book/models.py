from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    authorC = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)

class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)