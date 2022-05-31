from unittest.util import _MAX_LENGTH
from django.db import models
#from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.


class Userpost(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    text = models.TextField()
    due_date = models.DateField(auto_now=True)

    def __str__(self):
        return  self.title


class Ranking(models.Model):
    name_course = models.CharField(max_length=30)
    opinion = models.TextField()
    score = models.IntegerField()
    author = models.CharField(max_length=30)
    due_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name_course
