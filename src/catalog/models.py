from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()


class Author(models.Model):
    name = models.CharField(max_length=250)
    books = models.ManyToManyField(Book, related_name='authors')
